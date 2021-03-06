from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Si elimina el User, elimina los post 'Cascade'
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    # La vista despues de crear el post es el post: 

    # def get_absolute_url(self):
    #     return reverse('article-detail', args=(str(self.id)))
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
    

    def __str__(self):
        return str(self.user)



