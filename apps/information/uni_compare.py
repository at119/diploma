from apps.information.models import University
from django.conf import settings


class Compare(): 


    def __init__(self, request):
        self.session = request.session
        compare = self.session.get(settings.COMPARE)
        if not compare:  # if session is empty (first visit), create new compare session
            compare = self.session[settings.COMPARE]=[]
        self.compare = compare


    def add_uni(self, uni_id):
        if uni_id not in self.compare:
            self.compare.append(uni_id)
        self.save()

    
    def remove_uni(self, uni_id):
        if uni_id in self.compare:
            self.compare.remove(uni_id)
        self.save()

    def clear(self):
        self.compare.clear()
        self.save()


    def save(self):
        self.session.modified = True

    @property
    def unis(self):
        uni_ids = self.compare
        unis = University.objects.filter(id__in=uni_ids)
        return unis

    @property
    def ordered_unis(self):
        """Universities in the order they were added, with admission loaded."""
        if not self.compare:
            return []
        order = list(self.compare)
        unis = University.objects.filter(id__in=order).select_related("admission")
        by_id = {u.id: u for u in unis}
        return [by_id[i] for i in order if i in by_id]

    @property
    def winner(self):
        """University that wins by lowest total cost (price + cost of living). None if < 2 unis."""
        unis = self.ordered_unis
        if len(unis) < 2:
            return None
        return min(
            unis,
            key=lambda u: float(u.price_out or 0) + float(u.cost_of_living or 0),
        )

    @property
    def winner_others_names(self):
        """Names of universities that lost (for "Against: A, B" display)."""
        if not self.winner:
            return []
        return [u.name for u in self.ordered_unis if u.id != self.winner.id]


    def __iter__(self):
        uni_ids = self.compare
        unis = University.objects.filter(id__in=uni_ids)
        for uni in unis:
            yield uni

    
