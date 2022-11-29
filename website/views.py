from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
def http_test(request):
    return HttpResponse('<h1>This is a test </h1>')
def json_test(request):
    return JsonResponse({'name': 'ali'})
def home_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return HttpResponse('<h1>About Page</h1>')
def contact_view(request):
    return HttpResponse('<h1>Contact Page</h1>')