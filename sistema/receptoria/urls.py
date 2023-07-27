from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    #path('', views.inicio, name='inicio'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('roles', views.roles, name='roles'),
    path('cobros', views.cobros, name='cobros')
]