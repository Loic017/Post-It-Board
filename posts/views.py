from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from .forms import PostForm

# Create your views here.

def create(request):
    template = "create.html"
    context = {
        "form": PostForm()
    }
    return render(request, template, context)

