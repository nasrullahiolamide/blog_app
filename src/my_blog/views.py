from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.



# def index(request):
#     return HttpResponse("Hello there!")


class BlogListView(ListView):
    model = Post
    template_name = 'index.html' 
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'view_more.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name ='delete.html'
    success_url = reverse_lazy('home') 


