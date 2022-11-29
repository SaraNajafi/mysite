
from django.urls import path
from website.views import *
urlpatterns = [
    #path('url address, 'view', name)
    path('http-test/',http_test),
    path('json-test/',json_test),
    path('',home_view),
    path('about',about_view),
    path('contact',contact_view)
]
