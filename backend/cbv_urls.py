from django.urls import path
from backend import cbv_views

app_name='backend'

urlpatterns = [
    path('', cbv_views.login_view, name='login_view'),
    path('add-post/', cbv_views.AddPost.as_view(), name='add_post'),
    path('edit-post/<int:pk>/', cbv_views.EditPost.as_view(), name='edit_post'),
    path('show-post/', cbv_views.ListPost.as_view(), name='show_post'),
    path('delete-post/<int:pk>', cbv_views.DeletePost.as_view(), name='del_post'),
    path('detail-post/<int:pk>', cbv_views.DetailPost.as_view(), name='detail_post'),
    path('logout-page/', cbv_views.logout_view, name='logout_view'),
    path('backoffice/', cbv_views.dashboard, name='dashboard'),
    path('register-page/', cbv_views.register, name='register'),
    
]





