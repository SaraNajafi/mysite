from django import template

from blog.models import Post
from blog.models import Category

register = template.Library()

@register.simple_tag
def function(a):
    return a+2

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts': posts}



@register.inclusion_tag('blog/popular-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:5]
    return {'posts': posts}

@register.inclusion_tag('blog/post-categories.html')
def postcategories():
    posts= Post.objects.filter(status=1)
    categories= Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()

    return {'categories':cat_dict}