from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post


class Blog_App_Views(ListView):
    model = Post
    template_name = 'blog.html'

