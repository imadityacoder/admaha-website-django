from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = AutoSlugField(populate_from='name',unique=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

class Blog(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = AutoSlugField(populate_from='title',unique=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    img = models.ImageField(upload_to="images/")
    body =   RichTextField(blank=True,null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse("detailview", kwargs={"slug": self.slug})


