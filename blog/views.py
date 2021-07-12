from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ( 
    ListView,
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView
    )


from .models import Post


# Create your views here.

class BlogListView(ListView): # new for ListView
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # new for DetailView 
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['tital', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['tital', 'body']
    success_url = reverse_lazy('home') #redirect url link

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home') #redirect url link 