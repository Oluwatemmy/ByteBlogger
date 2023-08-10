from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Byte Blogger Home Page</h1>")

def about(request):
    return HttpResponse("<h1>Byte Blogger About Page</h1>")