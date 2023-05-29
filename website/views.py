from django.shortcuts import render
from blog.models import Post
from website.models import Contact
from website.forms import NameForm
# Create your views here.
from django.http import HttpResponse,JsonResponse
def http_test(request):
    return HttpResponse('<h1>This is a test </h1>')
def json_test(request):
    return JsonResponse({'name': 'ali'})
def home_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    return render(request,'website/contact.html')
def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    if request.method == 'POST':
        form=NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('done')
        
        
    form=NameForm()
    return render(request, 'test.html',{'form': form})