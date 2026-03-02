from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from apps.information.models import University
from .models import About, Major, Amina, Review, Major
from .forms import AboutForm, AminaForm,ContactForm, ReviewForm
from .utils import clean_wiki_text
from apps.information.uni_compare import Compare
# Create your views here.

from django.http import HttpResponse

# Create your views here.


def index(request):
    universities = University.objects.all()

    return render(request, "index.html", {"universities": universities})


class SearchListUni(ListView):
    template_name='uni_list.html'
    model=University
    context_object_name="universities"
    
    def get_queryset(self):
        search_text=self.request.GET.get('query')
        if search_text:
            return University.objects.filter(name__icontains=search_text)
        return University.objects.all()
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['search_text'] = self.request.GET.get('query')
        context['majors'] = Major.objects.all().order_by('name')
        return context
    
def about_page(request):
    about_p = About.objects.all()
    form = AboutForm()
    reviews = Review.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'about_p': about_p,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'about.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form data and send email (optional)
            # Return success message
            return redirect("index")
        
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


class UniDetailView(DetailView):
    template_name = "detail_uni.html"
    model = University


def major_list(request):
    majors = Major.objects.all().order_by('name')
    return render(request, 'major_list.html', {'majors': majors} )

def amina_page(request):
    amina_p = Amina.objects.all()
    form = AminaForm

    if request.method == 'POST':
        form = AminaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'amina_p': amina_p,
        'form': form,
    }
    return render(request, 'amina.html', context)

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'review.html', {'reviews': reviews})

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})


# views.py

def add_to_favorites(request, university_id):
    if not request.user.is_authenticated:
        from django.urls import reverse
        return redirect(reverse('sign_in') + '?next=' + request.get_full_path())
    university = University.objects.get(id=university_id)
    user = request.user
    user.list_uni.add(university)
    return redirect('favorites')

def remove_from_favorites(request, university_id):
    if not request.user.is_authenticated:
        from django.urls import reverse
        return redirect(reverse('sign_in') + '?next=' + request.get_full_path())
    university = University.objects.get(id=university_id)
    user = request.user
    user.list_uni.remove(university)
    return redirect('favorites')

@login_required(login_url='/accounts/login/')
def favorites(request):
    user = request.user
    favorite_universities = user.list_uni.all()
    return render(request, 'favorite.html', {'favorite_universities': favorite_universities})


def compare(request):
    params = request.GET.getlist('id')
    return render(request, 'compare.html')


def major_detail(request, pk):
    major = Major.objects.get(id=pk)
    # Clean text for display (citations, pronunciation, grammar). Pass cleaned data in context
    # so the template sees it — template's major.famous.all() would otherwise refetch from DB.
    try:
        major_description = clean_wiki_text(major.description) if major.description else (major.description or '')
    except Exception:
        major_description = major.description or ''
    famous_list = []
    try:
        for person in major.famous.all():
            famous_list.append({
                'person': person,
                'description': clean_wiki_text(person.description) if person.description else '',
                'action': clean_wiki_text(person.action) if person.action else '',
            })
    except Exception:
        famous_list = [{'person': p, 'description': p.description or '', 'action': p.action or ''} for p in major.famous.all()]
    # Temporarily set cleaned description on major so template {{ major.description }} works
    major.description = major_description
    context = {'major': major, 'famous_list': famous_list}
    return render(request, 'major_detail.html', context)

def error(request):
    return render(request, 'error.html', status=404)


def page_not_found(request, exception):
    """Custom 404 handler: show the same friendly error page."""
    return render(request, 'error.html', status=404)




def add_uni_to_compare(request, pk):
    compare = Compare(request)
    compare.add_uni(pk)
    return redirect("compare")


def remove_uni_from_compare(request, pk):
    compare = Compare(request)
    compare.remove_uni(pk)
    return redirect("compare")

def clear_compare(request):
    compare = Compare(request)
    compare.clear()
    return redirect("compare")


def geo_test(request):
    university = University.objects.all()
    uni = University.objects.all().first()

    context = {
        "universities": university,
        "uni": uni
    }
    return render(request, "map.html", context)