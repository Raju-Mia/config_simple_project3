from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

class BlogListView(ListView): # new for ListView
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # new for DetailView 
    model = Post
    template_name = 'post_detail.html'