from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import User



class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control uf-auth-input", "placeholder": "you@example.com"}),
        label="Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control uf-auth-input", "placeholder": "••••••••"}),
        label="Password",
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control uf-auth-input", "placeholder": "••••••••"}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control uf-auth-input", "placeholder": "••••••••"}), label="Confirm password")

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control uf-auth-input", "placeholder": "you@example.com"}),
            "first_name": forms.TextInput(attrs={"class": "form-control uf-auth-input", "placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control uf-auth-input", "placeholder": "Last name"}),
        }

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "birthday",
            "gender",
            "mobile",
            )
        widgets = {
            "email": forms.EmailInput(
                attrs={"class":"form-control"}
            ), 
            "first_name": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "birthday": forms.DateInput(
                attrs ={"class":"form-control", "type":"date"},
                format=("%Y-%m-%d")
            ),
            "gender":forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),
            "mobile": forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),
        }

