from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('suggest', views.Suggest.as_view(), name='suggest'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.RegisterUser.as_view(), name='register'),
]
