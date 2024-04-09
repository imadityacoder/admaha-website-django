# forms.py
from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = ['title', 'img']

class AddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title","category","author","img","body")
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "author":forms.Select(attrs={'class':'form-control'}),
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