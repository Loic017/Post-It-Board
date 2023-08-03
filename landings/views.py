from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from posts.models import Post

# Create your views here.

def landing(request):
    template = "landing.html"
    context = {}

    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user.id)
        context = {
            "posts": posts
        }
    return render(request, template, context)

def faq(request):
    template = "faq.html"
    return render(request, template)

def pricing(request):
    template = "pricing.html"
    return render(request, template)

def logout_view(request):
    logout(request)
    return redirect("/")
