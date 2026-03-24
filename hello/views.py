from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        text=request.POST.get('text')
        print(name,email,subject,text)
        user=Contact(name=name, email=email, subject=subject, text=text)
        user.save()
    return render(request,"home.html")
