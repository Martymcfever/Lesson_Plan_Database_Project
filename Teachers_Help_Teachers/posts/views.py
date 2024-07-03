from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def add_function(request):
    return render(request, "add_function.html")

def search_function(request):
    return render(request, "search_function.html")