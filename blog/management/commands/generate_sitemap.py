# management/commands/generate_sitemap.py

from django.core.management.base import BaseCommand
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
import os
from blog.models import Blog, Category  # Adjust based on your model names

class Command(BaseCommand):
    help = 'Generates sitemap.xml file'

    def handle(self, *args, **kwargs):
        current_site = "www.admoha.com"
        posts = Blog.objects.all()
        categories = Category.objects.all()
        
        sitemap_content = render_to_string('sitemap_template.xml', {
            'site': current_site,
            'posts': posts,
            'categories': categories,
        })
        
        sitemap_path = os.path.join(settings.STATIC_ROOT, 'sitemap.xml')
        
        with open(sitemap_path, 'w') as f:
            f.write(sitemap_content)
        
        self.stdout.write(self.style.SUCCESS('Successfully generated sitemap.xml'))
