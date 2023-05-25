import datetime
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(published_date__lte= datetime.datetime.now())
    context= {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post=get_object_or_404(Post, id=pid, status=1)
    context={'post': post}
    return render(request, 'blog/blog-single.html', context)





def blog_test(request,pid):
    post=Post.objects.get(id=pid)
    post.counted_views=post.counted_views+1
    post.save()
    context= {'post': post}
    return render(request, 'test.html',context)