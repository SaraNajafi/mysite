
from django.urls import path
from website.views import *

app_name= 'website'
urlpatterns = [
    #path('url address, 'view', name)
    path('',home_view, name='home'),
    path('about',about_view, name='about'),
    path('contact',contact_view, name='contact'),
    path('elements',elements_view, name='elements'),
    path('test', test_view, name='test'),
    path('newsletter',newsletter_view, name='newsletter'),
]
