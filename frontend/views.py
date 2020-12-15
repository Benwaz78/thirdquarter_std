from django.shortcuts import render, get_object_or_404, redirect
from frontend.models import Biography, Category, Post
from backend.forms import CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

# Create your views here.

def index(request):
    abt = Biography.objects.all()[:3]
    pst = Post.objects.order_by('-created')[:3]
    context = {
        'about':abt,
        'post':pst
    }
    return render(request, 'frontend/index.html', context)


def about(request):
    profile = Biography.objects.all()
    return render(request, 'frontend/about.html', {'bio':profile})

def detail_about(request, abt_id):
    detail = Biography.objects.get(id=abt_id)
    return render(request, 'frontend/detail.html', {'about_detail':detail})

def service(request):
    return render(request, 'frontend/services.html')

def blog(request):
    all_post = Post.objects.order_by('-created')
    return render(request, 'frontend/blog.html', {'post':all_post})

def single_blog(request, pk):
    single = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = single
            comment.save()
            return redirect('frontend:single_blog', pk=single.pk)
    else:
        form = CommentForm()
    return render(request, 'frontend/single-blog.html', {'detail':single, 'form':form})


def contact(request):
    return render(request, 'frontend/contact.html')

