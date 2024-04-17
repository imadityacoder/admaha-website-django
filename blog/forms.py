# forms.py
from django import forms
from .models import Blog ,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'img']

class AddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title","category","img","body")
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "category":forms.Select(attrs={'class':'form-control'}),
            "img":forms.FileInput(),
            "body":forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title","category","img","body")
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "category":forms.Select(attrs={'class':'form-control'}),
            "img":forms.FileInput(),
            "body":forms.Textarea(attrs={'class':'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "message":forms.Textarea(attrs={'class':'form-control'}),
            
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



