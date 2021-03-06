from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is homepage')






def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Message sent!')
    
    return render(request, 'contact.html')

