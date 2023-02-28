from django.urls import path

from . import views

urlpatterns = [
    path('', views.allBlogs),
   
    #path('<str:slug>', views.check),
    
    ]