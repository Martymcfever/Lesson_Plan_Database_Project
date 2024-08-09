"""@package docstring 
views.py 
File that holds methods of how webpages and functions are done on the website
"""

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect, FileResponse
from .models import Post



"""Home method that displays the homepage of the webpage"""
def home(request):
    return render(request, "home.html")

"""Plans method gives lesson_plans.htmnl the list of objects in Post Model"""
def plans(request):
    lesson_plan_list = Post.objects.all()
   
    return render(request, "lesson_plans.html", {'lesson_plan_list': lesson_plan_list})

"""one_lesson_plan method shows all titles of lesson plans on a single path of the webpage"""
def one_lesson_plan(request):
    one_plan = Post.objects.all()
   
    return render(request, "one_lesson_plan.html", {'one_plan': one_plan})

"""show_lesson_plan gives comprehensive view of a single lesson plan"""
def show_lesson_plan(request, plan_id):
    lesson_plan = Post.objects.get(pk=plan_id)
    
    return render(request, "show_lesson_plan.html", {'lesson_plan': lesson_plan})

def download_file(request, plan_id):
    plan = Post.objects.get(id = plan_id)
    filename = plan.lesson_plan.url
    response = FileResponse(open(filename, 'rb'))
    return response

"""add_function uses PostForm to form add objects to Post Model.
Tests if the form is valid determine if PostForm is complete
"""
def add_function(request):
    if (request.method == "POST"):
        form = PostForm(request.POST,request.FILES)
        if(form.is_valid()):
            post = form.save(commit= False)
            post.pub_date = timezone.now()
            post.save()
            return redirect(add_function)
    else:
        form = PostForm()
            
    return render(request, "add_function.html", {'form': form} )

def lesson_plan_detail(request, id):
    lesson_plan = get_object_or_404(Post, id=id)
    return render(request, 'show_lesson_plan.html', {'lesson_plan': lesson_plan})

"""add_comment uses CommentForm which links to to the PostForm adding the comments to the bottom of Posts.
   Tests itself to see if the form is complete otherwise it refreshes the add_comment page 
"""
def add_comment(request, id):
    lesson_plan = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lesson_plan = lesson_plan  # Set the foreign key
            comment.save()
            return render(request, "show_lesson_plan.html", {'lesson_plan': lesson_plan})
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form, 'lesson_plan': lesson_plan})

    
"""search_function allows for the search bar on the webpage to work"""
def search_function(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Post.objects.filter(title__contains=searched) | Post.objects.filter(grade_level__contains=searched) | Post.objects.filter(subject__contains=searched)

        return render(request, "search_function.html",{'searched':searched, 'results':results})
    else:
        return render(request, "search_function.html")