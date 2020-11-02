from django.urls import path
from backend import views

app_name='backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout-page/', views.logout_view, name='logout_view'),
    path('backoffice/', views.dashboard, name='dashboard'),
    path('register-page/', views.register, name='register'),
    path('confirm-page/', views.confirm_logout, name='confirm_logout'),
    path('add-category/', views.categroy_form, name='categroy_form'),
    path('add-post/', views.post_form, name='post_form'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('view-post-byuser/', views.view_post_byuser, name='view_post_byuser'),
    path('list-users/', views.list_users, name='list_users'),
    path('view-categories/', views.view_categories, name='view_categories'),
    path('view-profile/', views.view_profile, name='view_profile'),
]





