from django.shortcuts import render, redirect
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Post

def home(request):
    return render(request, "home.html")

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
        results = Post.objects.filter(name__contains=searched)

        return render(request, "search_function.html",{'searched':searched, 'results':results})
    else:
        return render(request, "search_function.html")