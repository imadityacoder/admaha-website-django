from django.contrib import admin
from .models import Category,Blog,Contact
# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Contact)

