from apps.information.models import University
from django.conf import settings


class Compare(): 


    def __init__(self, request):
        self.session = request.session
        compare = self.session.get(settings.COMPARE)
        if not compare: #если сессис пустая и человек первые на сайте  , то создается новая сессия cart
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


    def __iter__(self):
        uni_ids = self.compare
        unis = University.objects.filter(id__in=uni_ids)
        for uni in unis:
            yield uni

    
