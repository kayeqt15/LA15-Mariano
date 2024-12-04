from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def say_hello(request):
    return HttpResponse("Hello Django")

def say_hi(request):
    return render(request, 'hi.html', {'name': 'Jeorge Bryan V. Domingo'})

def blog_list(request):
    posts = Post.objects.all()  # Retrieve all Post objects
    context = {
        'blog_list': posts  # Pass the posts to the template
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Fetch the post by id
    context = {'post': post}
    return render(request, 'app1/blog_detail.html', context)
