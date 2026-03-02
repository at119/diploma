from django.urls import path

from apps.accounts import views

from .views import *

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="sign_in"),
    path("logout/",views.user_logout, name="logout"),

    path("sign_up/", views.register_user, name="sign_up"),
    path('profile/<int:pk>/', views.UserUpdateProfile.as_view(), name="profile" ),
    path('change_password/', views.change_password, name='change_password'),
    path("uni_search/", UniSearchView.as_view(), name="uni_search"),
]
