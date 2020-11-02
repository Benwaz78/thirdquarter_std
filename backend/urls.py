from django.urls import path
from backend import views

app_name='backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('backoffice/', views.dashboard, name='dashboard'),
    path('register-page/', views.register, name='register'),
    path('add-category/', views.categroy_form, name='categroy_form'),
    path('add-post/', views.post_form, name='post_form'),
    path('list-users/', views.list_users, name='list_users'),
    path('view-categories/', views.view_categories, name='view_categories')
]





