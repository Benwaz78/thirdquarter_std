from django.urls import path
from frontend import views

app_name='frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('service-page/', views.services, name='services'),
    path('contact-us/', views.contact, name='contact')

]