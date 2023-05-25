from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=True)
    context= {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')

def blog_test(request, name,family,age):
    context= {'name': name, 'family':family, 'age':age}
    return render(request, 'test.html', context)