from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json


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
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Post Created')
    else:
        post_form = PostForm()
    return render(request, 'backend/add-post.html', {'post': post_form})

@login_required(login_url='/dashboard/')
def edit_post(request, post_id):
    get_post =get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=get_post)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Post Edited')
    else:
        post_form = PostForm(instance=get_post)
    return render(request, 'backend/edit-post.html', {'edit': post_form})

@login_required(login_url='/dashboard/')
def delete_post(request, post_id):
    single_post = get_object_or_404(Post, pk=post_id)
    single_post.delete()
    return redirect('backend:view_post_byuser')

@login_required(login_url='/dashboard/')
def filter_post(request):
    post = FilterForm(request.GET)
    queryset = Post.objects.all()
    if post.is_valid():
        user=post.cleaned_data.get('user')
        category=post.cleaned_data.get('category')
        if user and category:
            queryset = queryset.filter(user__username=user, category__cat_name=category)
    return render(request, 'backend/filter-post.html', {'query':queryset, 'post':post})
    
def view_post_byuser(request):
    user_post = Post.objects.filter(user=request.user)
    return render(request, 'backend/post-byuser.html', {'post':user_post})

@login_required(login_url='/dashboard/')
def list_users(request):
    show_user = User.objects.all().order_by('last_name')
    return render(request, 'backend/view-users.html', {'users':show_user})

@login_required(login_url='/dashboard/')
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
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

@login_required(login_url='/dashboard/')
def confirm_logout(request):
    return render(request, 'backend/confirm-logout.html')

@login_required(login_url='/dashboard/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')

@login_required(login_url='/dashboard/')
def view_profile(request):
    return render(request, 'backend/view-profile.html')


def search_page(request):
    return render(request, 'frontend/search-page.html')



def search(request):
    if request.method=='GET':
        q = request.GET.get('search')
        if q is not None:
            q = request.GET.get('search')
            search_qs = Post.objects.filter(pst_title__contains=q)
            print(search_qs)
        else:
            search_qs = []
        return render(request, 'frontend/search-result.html', {'data':search_qs})
    
    