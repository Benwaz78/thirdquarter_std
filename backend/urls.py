from django.urls import path
from backend import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register-page/', views.register, name='register')
]




