# forms.py
from django import forms
from .models import Blog ,Contact


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


class signupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':"username"}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':"password"}),

        }

