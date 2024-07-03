from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add", views.add_function, name="add"),
    path("search", views.search_function, name="search"),     
]