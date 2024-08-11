## @package docstring
#  views.py
#  File that holds methods of how webpages and functions are done on the website

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect, FileResponse
from .models import Post
import random
from django.conf import settings
import os



## Home method that displays the homepage of the webpage
def home(request):
    return render(request, "home.html")

## Plans method gives lesson_plans.htmnl the list of objects in Post Model
def plans(request):
    lesson_plan_list = Post.objects.all()
   
    return render(request, "lesson_plans.html", {'lesson_plan_list': lesson_plan_list})

## one_lesson_plan method shows all titles of lesson plans on a single path of the webpage
def one_lesson_plan(request):
    one_plan = Post.objects.all()
   
    return render(request, "one_lesson_plan.html", {'one_plan': one_plan})

## show_lesson_plan gives comprehensive view of a single lesson plan
def show_lesson_plan(request, plan_id):
    lesson_plan = Post.objects.get(pk=plan_id)
    
    return render(request, "show_lesson_plan.html", {'lesson_plan': lesson_plan})

## download_file gives the file url to allow downloads to occur
def download_file(request, plan_id):
    plan = get_object_or_404(Post,id = plan_id)
    filename = plan.lesson_plan.path
    response = FileResponse(open(filename, 'rb'))
    return response

## add_function uses PostForm to add objects to Post Model
#  Tests if the form is valid to determine if PostForm is complete
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

## lesson_plan_detail renders a single Post model object to show in show_lesson_plan.html
def lesson_plan_detail(request, id):
    lesson_plan = get_object_or_404(Post, id=id)
    return render(request, 'show_lesson_plan.html', {'lesson_plan': lesson_plan})


## add_comment uses CommentForm to add objects to comment Model
#  Tests if the form is valid to determine if CommentForm is complete
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

    
##search_function allows for the search bar on the webpage to workw
def search_function(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Post.objects.filter(title__contains=searched) | Post.objects.filter(grade_level__contains=searched) | Post.objects.filter(subject__contains=searched)

        return render(request, "search_function.html",{'searched':searched, 'results':results})
    else:
        return render(request, "search_function.html")

##random_image function allows the home page to display a random image upon entering the webpage
def pic_home(request):
    # Assuming your "Uploaded Files" folder is in the 'media' directory at the root level
    uploaded_files_dir = os.path.join(settings.BASE_DIR, 'media', 'Uploaded Files')

    # Check if the directory exists
    if not os.path.exists(uploaded_files_dir):
        return HttpResponse("Uploaded Files directory not found.", status=404)

    images = [f for f in os.listdir(uploaded_files_dir) if os.path.isfile(os.path.join(uploaded_files_dir, f))]
    random_image = random.choice(images) if images else None
    random_image_url = os.path.join(settings.MEDIA_URL, 'Uploaded Files', random_image) if random_image else None

    context = {
        'random_image_url': random_image_url,
    }
    return render(request, 'home.html', context)