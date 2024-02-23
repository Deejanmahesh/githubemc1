from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def Message(request):
    return render(request,"Message.html")

def success(request):
    messages.success(request,"this is success message")
    return render(request,"Message.html")

def info(request):
    messages.info(request,"this Info message")
    return render(request,"Message.html")

def error(request):
    messages.error(request,"this Error message")
    return render(request,"Message.html")

def warning(request):
    messages.warning(request,"this Warning message")
    return render(request,"Message.html")
