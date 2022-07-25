from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Post
from django.views import generic


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(generic.DetailView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(generic.DeleteView):
    model = Post
    fields = ("__all__")
    success_url = reverse_lazy("blog:all")

class PostListView(generic.ListView):
    model = Post