from django.shortcuts import render
from myceleryproject.celery import add

def index(request):
    print("Results: ")
    add(10,20)
    return render(request,"home.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')