from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('services-page/', views.service, name='service')
]
