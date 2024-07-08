from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    title = forms.TextInput()
    contributors = forms.TextInput()
    grade_level = forms.TextInput()
    subject = forms.TextInput()
    description = forms.Textarea()
    lesson_plan = forms.FileField()
    
    class Meta:
        model = Post
        fields = ('title','contributors','grade_level','subject','description','lesson_plan')