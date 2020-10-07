from django.shortcuts import render
from frontend.models import Biography

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')


def about(request):
    profile = Biography.objects.all()
    return render(request, 'frontend/about.html', {'bio':profile})

def service(request):
    return render(request, 'frontend/services.html')
