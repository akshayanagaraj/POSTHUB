from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .forms import PostForm
from .models import Post


def home(request):
    data = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/home.html', context=data)


def about(request):
    return HttpResponse('about')


def create_post(request):
    form = PostForm()
    data = {
        'form': form,
    }
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my-posts-url')
    return render(request, template_name='blog/create_post.html', context=data)


def all_posts(request):
    data = {
        'Posts': Post.objects.all()
    }
    if request.method == "POST":
        print(request.POST)
        id = int(request.POST['button'])
        print(id)
        obj = get_object_or_404(Post, id=id )
        obj.delete()
        return redirect('my-posts-url')

    return render(request, template_name='blog/my_posts.html', context=data)


def detail(request, id):
    obj = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=obj)
    data = {
        'form': form,
    }
    if request.method == "POST" :

        if form.is_valid():
            form.save()
            return redirect('my-posts-url')

    return render(request, template_name="blog/detail.html", context=data)
