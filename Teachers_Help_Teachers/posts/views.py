from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def add_function(request):
    return render(request, "add_function.html")

def search_function(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Posts.objects.filter(name__contains=searched)

        return render(request, "search_function.html",{'searched':searched, 'results':results})
    else:
        return render(request, "search_function.html")