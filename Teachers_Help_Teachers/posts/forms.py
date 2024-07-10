from django import forms
from django.forms import ModelForm
from .models import Post

#Create Post form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"