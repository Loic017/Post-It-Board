from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def save(self, commit=True, author=None):
        post = super().save(commit=False)
        if author:
            post.author = author
        if commit:
            post.save()
        return post