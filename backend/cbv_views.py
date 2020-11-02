from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import(
    ListView, CreateView,
    UpdateView, DetailView,
    DeleteView
)

from frontend.models import *
from backend.forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse_lazy




def register(request):
    if request.method == 'POST':
        register = Register(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'User have been registered')
    else:
        register = Register()
    return render(request, 'frontend/register.html', {'reg':register})

class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/dashboard/'
    models = Post
    template_name = 'backend/add-post.html'
    form_class = PostForm
    success_url = reverse_lazy('backend:add_post')
    success_message = 'Post added successfully'

class EditPost(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/dashboard/'
    models = Post
    template_name = 'backend/add-post.html'
    form_class = PostForm
    success_url = reverse_lazy('backend:add_post')
    success_message = 'Post Edited successfully'

class ListPost(LoginRequiredMixin, SuccessMessageMixin, ListView):
    login_url = '/dashboard/'
    models = Post
    template_name = 'backend/list-post.html'
    context_object_name= 'list_post'

class DetailPost(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    login_url = '/dashboard/'
    models = Post
    template_name = 'backend/detail-post.html'
    context_object_name= 'detail_post'

class DeletePost(DeleteView):
    model = Post
    template_name = 'form_app/confirm_delete.html'
    success_url = reverse_lazy('backend:show_post')

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