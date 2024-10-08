## @packge docstring
#  urls.py
#  list of paths that is utilized for the webpage

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

## urlpattern list that holds paths of urls
urlpatterns = [

    path('', views.home, name='home'),
    path("", views.pic_home, name="pic_home"),
    path('Lesson Plans', views.plans, name="plans"),
    path("add", views.add_function, name="add"),
    path("search", views.search_function, name="search"),     
    path("one_lesson_plan", views.one_lesson_plan, name="one_plan"),
    path("show_lesson_plan/<plan_id>", views.show_lesson_plan, name="show_plan"),
    path("download/<plan_id>", views.download_file, name="download"),
    path("show_lesson_plan/<int:id>/add-comment", views.add_comment, name='add_comment'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)