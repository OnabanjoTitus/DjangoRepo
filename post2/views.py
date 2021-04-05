from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from post2.models import Post


class HomePageViews(ListView):
    model = Post
    template_name = 'posts2.html'
    context_object_name = 'all_posts_list'
