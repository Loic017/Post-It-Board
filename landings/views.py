from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def landing(request):
    template = loader.get_template("landing.html")
    return HttpResponse(template.render())

def faq(request):
    template = loader.get_template("faq.html")
    return HttpResponse(template.render())

def pricing(request):
    template = loader.get_template("pricing.html")
    return HttpResponse(template.render())