from django.urls import path
from blog.views import *

app_name= 'blog'
urlpatterns = [
    #path('url address, 'view', name)
    path('',blog_view, name='blog'),
    path('<int:pid>', blog_single, name='single'),
    #path('post-<int:pid>', blog_test, name='test')
    
]
