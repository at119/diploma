from django.contrib import admin

from apps.accounts.models import User

# Register your models here.
from apps.accounts.forms import UserRegisterForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserRegisterForm
    list_display = ["username", "email"]