from django.shortcuts import render
from django.http import HttpResponse

from backend.forms import *

# Create your views here.
def login(request):
    return HttpResponse('<h1>Login Page</h1>')


def register(request):
    return HttpResponse('<h1>Register Page</h1>')


def dashboard(request):
    return render(request, 'backend/index.html')

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

