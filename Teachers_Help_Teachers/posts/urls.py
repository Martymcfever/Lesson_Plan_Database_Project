from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('Lesson Plans', views.plans, name="plans"),
    path("add", views.add_function, name="add"),
    path("search", views.search_function, name="search"),     
    path("one_lesson_plan", views.one_lesson_plan, name="one_plan"),
    path("show_lesson_plan/<plan_id>", views.show_lesson_plan, name="show_plan"),   
    
]