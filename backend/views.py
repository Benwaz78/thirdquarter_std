from django.shortcuts import render, redirect
from django.http import HttpResponse


from frontend.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/dashboard/')
def categroy_form(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, 'Category Created')
    else:
        cat_form = CategoryForm()
    return render(request, 'backend/add-category.html', {'cat':cat_form})

@login_required(login_url='/dashboard/')
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


@login_required(login_url='/dashboard/')
def dashboard(request):
    return render(request, 'backend/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:index')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

@login_required(login_url='/dashboard/')
def confirm_logout(request):
    return render(request, 'backend/confirm.html')

@login_required(login_url='/dashboard/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')