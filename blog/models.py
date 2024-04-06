from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = AutoSlugField(populate_from='name',unique=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Blog(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = AutoSlugField(populate_from='title',unique=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    body =   HTMLField()
    img = models.ImageField(upload_to="images/")
    publish_on = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
