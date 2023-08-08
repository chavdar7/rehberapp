from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def kisilist(request):
    return render(request, "kisilist", {})

def kisiekle(request):
    return render(request, "kisiekle", {})