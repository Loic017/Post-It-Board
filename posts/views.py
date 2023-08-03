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

    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user.id
                post.save()
                return redirect("landing")

    return render(request, template, context)

