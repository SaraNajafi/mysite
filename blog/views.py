from contextlib import nullcontext
import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def blog_view(request, cat_name=None, author_username=None, **kwargs):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    if cat_name != None:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=1)
    prev = post
    next = post
    if not post.login_require:
        blogs = Post.objects.filter(status=1)
        for i in range(len(blogs)):
            if blogs[i].id == post.id:
                print(len(blogs))
                if i == 0:
                    print(blogs[i].title)
                    prev = '0'
                    next = blogs[i+1]
                elif i == len(blogs)-1:
                    print(i)
                    print(blogs[i].title)
                    prev = blogs[i-1]
                    next = '0'
                else:
                    prev = blogs[i-1]
                    next = blogs[i+1]

        context = {'post': post, 'prev': prev, 'next': next}
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_test(request):
    # post=Post.objects.get(id=pid)
    # post.counted_views=post.counted_views+1
    # post.save()
    # context= {'post': post}
    return render(request, 'test.html')


def blog_search(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    # print(request)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
