from django.shortcuts import render, redirect, HttpResponse
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponseRedirect, FileResponse
from .models import Post




def home(request):
    return render(request, "home.html")


def plans(request):
    lesson_plan_list = Post.objects.all()
   
    return render(request, "lesson_plans.html", {'lesson_plan_list': lesson_plan_list})


def one_lesson_plan(request):
    one_plan = Post.objects.all()
   
    return render(request, "one_lesson_plan.html", {'one_plan': one_plan})

def show_lesson_plan(request, plan_id):
    lesson_plan = Post.objects.get(pk=plan_id)
    
    return render(request, "show_lesson_plan.html", {'lesson_plan': lesson_plan})

def download_file(request, plan_id):
    plan = Post.objects.get(id = plan_id)
    filename = plan.lesson_plan.url
    response = FileResponse(open(filename, 'rb'))
    return response


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
    

def search_function(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Post.objects.filter(title__contains=searched)

        return render(request, "search_function.html",{'searched':searched, 'results':results})
    else:
        return render(request, "search_function.html")