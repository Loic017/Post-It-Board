from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.

@login_required
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

@login_required
def favourite(request, id):
    post = get_object_or_404(Post, id=id)
    
    if post.isFavourite:
        post.isFavourite = False
    else:
        post.isFavourite = True
    post.save()
    return redirect("landing")

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("landing")

@login_required
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    template = "edit.html"   
    form = PostForm(instance=post)
    context = {
        "form": form,
    }

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect("landing")
        
    return render(request, template, context)

def sharePost(request, id):
    post = get_object_or_404(Post, id=id)
    template = "share.html"
    context = {
        "post": post,
    }

    return render(request, template, context)