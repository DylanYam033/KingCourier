from django.urls import path
from login import views
from user.views import user_create, users_list

urlpatterns = [
    path('', views.login_user, name='login'),
    path('users/', users_list, name='users'),
    path('perfil/', views.perfil, name='perfil'),
    path('users/create', user_create, name='register'),
    path('logout/', views.log_out, name='logout'),
]
