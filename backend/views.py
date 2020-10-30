from django.shortcuts import render
from django.http import HttpResponse


from frontend.models import *

from backend.forms import *

from django.contrib.auth.models import User

from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        register = Register(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'User have been registered')
    else:
        register = Register()
    return render(request, 'frontend/register.html', {'reg':register})

def categroy_form(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, 'Category Created')
    else:
        cat_form = CategoryForm()
    return render(request, 'backend/add-category.html', {'cat':cat_form})
    
def post_form(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Post Created')
    else:
        post_form = PostForm()
    return render(request, 'backend/add-post.html', {'post': post_form})


def list_users(request):
    show_user = User.objects.all().order_by('last_name')
    return render(request, 'backend/view-users.html', {'users':show_user})

def view_categories(request):
    show_cat = Category.objects.all()
    return render(request, 'backend/view-categories.html', {'cat':show_cat})


def dashboard(request):
    return render(request, 'backend/index.html')

def login(request):
    return HttpResponse('<h1>Login Page</h1>')
