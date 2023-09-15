from django.urls import path

from apps.information import views

from django.contrib import admin
from django.urls import path
from .views import major_list

urlpatterns = [
    path("", views.index, name="index"),
    path("uni/list/", views.SearchListUni.as_view(), name="uni_list"),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail/uni/<int:pk>', views.UniDetailView.as_view(), name="detail_uni"),
    path('major/list', views.major_list, name="major_list" ),
    path('amina/', views.amina_page, name='amina'),
    path('review/', views.review_list, name='review'),
    path('reviews/create/', views.create_review, name='create_review'),
    path('add_to_favorites/<int:university_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:university_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites, name='favorites'),
    path('compare/', views.compare, name="compare"),
    path('major/detail/<int:pk>/', views.major_detail, name="major_detail"),
    path('error/', views.error, name="error"),
    path("add/compare/<int:pk>", views.add_uni_to_compare, name="add_compare"),
    path("remove/compare/<int:pk>/", views.remove_uni_from_compare, name="remove_compare"),
    path("clear/compare/", views.clear_compare, name="clear_compare"),
    path("map/", views.geo_test, name="map")

    ]

