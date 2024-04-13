# forms.py
from django import forms
from .models import Blog #,Contact


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


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ('name', 'email', 'phone', 'message')
#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             "email":forms.EmailInput(attrs={'class':'form-control'}),
#             'phone':forms.NumberInput(attrs={'class':'form-control'}),
#             "message":forms.Textarea(attrs={'class':'form-control'}),
            
#         }
