from django.contrib import admin

# Register your models here.
from .models import University, Major,Admission, Professor, UniversityRating, Review, FamousPeople
from .forms import UniCreateForm


class ProfessorInline(admin.StackedInline):
    model = Professor
    extra = 2

class AdminssionInline(admin.StackedInline):
    model = Admission
    extra = 1
    max_num = 1

class FamousPeopleInline(admin.StackedInline):
    model = FamousPeople
    extra = 1

@admin.register(University)
class UniAdmin(admin.ModelAdmin):
    form = UniCreateForm
    inlines = [AdminssionInline, ProfessorInline]
    list_display = ["name", "location", "type", "dorm", "type"]
    filter_horizontal = ["majors"]

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    inlines = [FamousPeopleInline]
    list_display = ["name", "hard_or_easy", "popularity", "description", "img"]
    list_filter = ["hard_or_easy", "popularity", "description", "img"]
    

@admin.register(UniversityRating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["university", "rating"]
    list_filter = ["rating"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["author", "content", "created_at"]
    list_filter =  ["content"]