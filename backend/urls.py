from django.urls import path
from backend import views

app_name='backend'

urlpatterns = [
    path('', views.login, name='login'),
    path('backoffice/', views.dashboard, name='dashboard'),
    path('register-page/', views.register, name='register'),
    path('add-category/', views.categroy_form, name='categroy_form'),
    path('add-post/', views.post_form, name='post_form')
]





