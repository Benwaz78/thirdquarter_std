from django.urls import path
from frontend import views

<<<<<<< HEAD
app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('detail-page/<int:abt_id>/', views.detail_about, name='detail_about'),
    path('services-page/', views.service, name='service'),
    path('single-page/<int:post_id>', views.single_blog, name='single_blog'),
    path('blog', views.blog, name='blog')
]
=======
app_name='frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('service-page/', views.services, name='services'),
    path('contact-us/', views.contact, name='contact')

]
>>>>>>> fc2b3107a1a59876ede3fd3535367180c289c8e5
