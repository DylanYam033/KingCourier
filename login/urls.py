from django.urls import path
from login import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
    path('register/', views.user_create, name='register'),
]
