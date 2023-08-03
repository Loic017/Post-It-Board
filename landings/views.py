from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

# Create your views here.

def landing(request):
    template = "landing.html"
    return render(request, template)

def faq(request):
    template = "faq.html"
    return render(request, template)

def pricing(request):
    template = "pricing.html"
    return render(request, template)

def logout_view(request):
    logout(request)
    return redirect("/")
