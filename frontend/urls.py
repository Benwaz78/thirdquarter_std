from django.urls import path
from frontend import views
app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('detail-page/<int:abt_id>/', views.detail_about, name='detail_about'),
    path('services-page/', views.service, name='service'),
    path('single-page/<int:post_id>', views.single_blog, name='single_blog'),
    path('blog', views.blog, name='blog'),
    path('contact-page/', views.contact, name='contact'),
]
