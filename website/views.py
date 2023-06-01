from django.shortcuts import render, redirect
from blog.models import Post
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsLetterForm
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
def http_test(request):
    return HttpResponse('<h1>This is a test </h1>')
def json_test(request):
    return JsonResponse({'name': 'ali'})
def home_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name='anonymous',
                email=form.cleaned_data.get('email'),
                subject =form.cleaned_data.get('subject'),
                message=form.cleaned_data.get('message')
            )
            #form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully')
            #messages.success(request, "Message sent." )
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, 'Invalid')
    form = ContactForm
    return render(request,'website/contact.html',{'form':form})


def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        
        
    form=ContactForm()
    return render(request, 'test.html',{'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    

