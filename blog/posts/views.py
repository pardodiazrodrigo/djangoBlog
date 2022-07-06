from unicodedata import category
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    #ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title','body') - Selecionar algunos fields del modelo

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title','body') - Selecionar algunos fields del modelo

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def CategoryView(request,cats):
    cats = cats.capitalize()
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    cats = cats.replace('-',' ')

    return render(request,'categories.html',{'cats':cats,'category_post':category_post})
