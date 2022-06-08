from django.shortcuts import render , HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

def index(request):
    #return HttpResponse("this is my home page")
    return render (request, 'index.html')


def about(request):
    #return HttpResponse("this is my about page")
    return render (request, 'about.html')

def service(request):
    #return HttpResponse("this is my service page")
    return render (request, 'service.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!.')
    
    #return HttpResponse("this is my contact page")
   
    
    
    return render (request, 'contact.html')



# Create your views here.
