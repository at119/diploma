from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from apps.information.models import University
from .models import About, Major, Amina, Review, Major
from .forms import AboutForm, AminaForm,ContactForm, ReviewForm
from apps.information.uni_compare import Compare
# Create your views here.

from django.http import HttpResponse

from django_admin_geomap import geomap_context

# from .forms import ComparisonForm


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
        context['majors'] = Major.objects.all()
        return context
    
def about_page(request):
    about_p = About.objects.all()
    form = AboutForm()

    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'about_p': about_p,
        'form': form,
    }
    return render(request, 'about.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы и отправка письма (по желанию)
            # Верните сообщение об успешной отправке формы
            return redirect("index")
        
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


class UniDetailView(DetailView):
    template_name = "detail_uni.html"
    model = University


def major_list(request):
    majors = Major.objects.all()
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
    reviews = Review.objects.all()
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
    university = University.objects.get(id=university_id)
    user = request.user
    user.list_uni.add(university)
    return redirect('favorites')

def remove_from_favorites(request, university_id):
    university = University.objects.get(id=university_id)
    user = request.user
    user.list_uni.remove(university)
    return redirect('favorites')

def favorites(request):
    user = request.user
    favorite_universities = user.list_uni.all()
    return render(request, 'favorite.html', {'favorite_universities': favorite_universities})


def compare(request):
    params = request.GET.getlist('id')
    return render(request, 'compare.html')


def major_detail(request, pk):
    # Получите объект факультета по его ID или другому уникальному идентификатору
    major = Major.objects.get(id=pk)
    context = {
        'major': major,
    }
    return render(request, 'major_detail.html', context)

def error(request):
    return render(request, 'error.html')




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