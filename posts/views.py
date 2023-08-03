from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

# Create your views here.

def create(request):
    template = "create.html"
    return render(request, template)

