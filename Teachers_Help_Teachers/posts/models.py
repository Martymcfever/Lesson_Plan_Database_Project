from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    contributors = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=2)
    subject = models.CharField(max_length = 25)
    description = models.CharField(max_length=250)
    lesson_plan = models.FileField(upload_to='Uploaded_Files/', null=True, max_length=254)