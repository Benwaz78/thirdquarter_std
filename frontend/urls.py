from django.urls import path
from frontend import views
app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('detail-page/<int:abt_id>/', views.detail_about, name='detail_about'),
    path('services-page/', views.service, name='service'),
    path('single-page/<int:pk>', views.single_blog, name='single_blog'),
    path('sidebar_search/', views.sidebar_search, name='sidebar_search'),
    path('blog', views.blog, name='blog'),
    path('contact-page/', views.contact, name='contact'),
]
