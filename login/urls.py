from django.urls import path
from login import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('register/', views.user_create, name='register'),
    path('logout/', views.log_out, name='logout'),
]
