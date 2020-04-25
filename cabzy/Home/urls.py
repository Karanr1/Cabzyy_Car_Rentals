
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('bookcab', views.bookcab, name = 'bookcab'),
    path('rides', views.rides, name = 'rides'),
    path('booking',views.booking, name = 'booking'),
     path('edit',views.edit, name = 'edit'),
]