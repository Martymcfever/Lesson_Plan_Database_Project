"""@package docstring 
model.py 
Creation of classes that are used as Django Models
Only class is Post
"""

from django.db import models

# Create your models here.
""" Class for Post Model 
Attributes: title, pub_date, contributors, grade_level, subject, description, lesson_plan, verified
Methods: __str__()
"""
class Post(models.Model):
    """Fields to desribe a post of a lesson plan
    """
    title = models.CharField(max_length=100, verbose_name= "title")
    pub_date = models.DateTimeField("date published", null=True)
    contributors = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=2)
    subject = models.CharField(max_length = 25)
    description = models.TextField()
    lesson_plan = models.FileField(upload_to='Uploaded_Files/', null=True)
    verified = models.BooleanField(default=False)

    """Allow Post to display as a title field
    """
    def __str__(self):
        return self.title  
