from django.urls import path
from backend import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register-page/', views.register, name='register')
]




