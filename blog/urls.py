from django.urls import path
from blog.views import *

app_name= 'blog'
urlpatterns = [
    #path('url address, 'view', name)
    path('',blog_view, name='blog'),
    path('single', blog_single, name='single'),
    path('<str:name>/<str:family>/<int:age>', blog_test, name='test')
    
]
