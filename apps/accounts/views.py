from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import FormView, UpdateView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.db.models import Q


from django.contrib.auth.mixins import LoginRequiredMixin


from apps.information.models import University
 
from apps.accounts.forms import UserRegisterForm, UserUpdateForm
from apps.accounts.forms import LoginForm
from apps.accounts.models import User

# Create your views here.

def get_login(request):
    return render(request, "login.html")


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data  # в cleaned_data хранятся данные из формы
        email = data["email"]
        password = data["password"]
        user = authenticate(self.request, email=email, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return redirect("index")
        else:
            return HttpResponse("Your email or password is incorrect.")

    def form_invalid(self, form):
        # Если форма недействительна, вы можете обработать это здесь
        return self.render_to_response(self.get_context_data(form=form))


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")




def register_user(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password1"]
            user = User.objects.create(
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"]
            )
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect("index")
    
    context = {'form':form}
    return render(request, 'register.html', context)



class UserUpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "profile.html"
    queryset = User.objects.all()
    form_class=UserUpdateForm
    success_url = reverse_lazy("index")
    

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        form = self.form_class(instance=user)
        universities = University.objects.all()
        context = {
            "user": user,
            "form":form,
            "universities": universities,
        }
        return render(request, "profile.html", context)


    def get_object(self):
        return self.request.user
    

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["edit_form"] = UserUpdateForm()
    #     return context
    # {% for uni in user.uni_list.all %}
    # {% endfor %}


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        previous_url = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            # messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect("profile", pk=request.user.pk)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


# def search(request):
#     form = SearchForm(request.GET)
#     results = []
#     if form.is_valid() and form.is_bound:
#         query = form.cleaned_data.get('query')
#         if query: 
#             results = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
#     return render(request, 'search.html', {'form': form, 'results': results})
 

class UniSearchView(ListView):  
    model = University
    template_name = "uni_search.html"
    paginate_by = 10
    
    def get_queryset(self):
        search_text = self.request.GET.get("query")
        q = self.model.objects.filter(name__icontains=search_text)
        return q
