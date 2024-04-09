from django.urls import path
from . import views

urlpatterns = [
    path('getBalance', views.get_balance, name='getBalance'),  # Without trailing slash
    path('getBalance/', views.get_balance, name='getBalance'),  # With trailing slash
    path('createTask', views.createTask, name='createTask'),  # Without trailing slash
    path('createTask/', views.createTask, name='createTask'),  # With trailing slash
]

