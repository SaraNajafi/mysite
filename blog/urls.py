from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    # path('url address, 'view', name)
    path('', blog_view, name='blog'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('test', blog_test, name='test'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('rss/feed', LatestEntriesFeed()),


]
