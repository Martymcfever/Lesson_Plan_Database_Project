## @package docstring
#  forms.py 
# 
#  File that creates the forms that allows the add functions of the Post and Comment forms to work 

from django import forms
from django.forms import ModelForm
from .models import Post, Comment

##PostForm class creates the form to allow the add_function to add objects to Post Model
class PostForm(ModelForm):

    ##Attributes of the Post Model that the form will ask for entries"
    title = forms.TextInput()
    contributors = forms.TextInput()
    grade_level = forms.TextInput()
    subject = forms.TextInput()
    description = forms.Textarea()
    lesson_plan = forms.FileField()
    
    ## Specifies the wanted model the form is using (Post)
    #  formats the form to allow a specific style of the widgets and labels on the webpage
    class Meta:
        model = Post
        fields = ('title','contributors','grade_level','subject','description','lesson_plan')
        widgets = { 'title':forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title'}), 
                   'contributors': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Contriubutors'}), 
                   'grade_level':forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Grade Level'}), 
                   'subject': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Subject Area'}),  
                   'description': forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Description of Item'}), }
        
        labels = { 'title':'', 
                   'contributors': '', 
                   'grade_level':'', 
                   'subject': '',  
                   'description': '' }

## Specifies the wanted model the form is using (Comment)
#  formats the form to allow a specific style of the widgets and labels on the webpage
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contributor'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }