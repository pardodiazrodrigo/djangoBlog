from tkinter import Widget
from django import forms
from .models import Post,Category

#choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]

choices = Category.objects.all().values_list('name','name')
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Put a title to your post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={ 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Put a title to your post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={ 'class': 'form-control'}),
        }
