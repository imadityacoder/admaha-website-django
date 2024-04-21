from blog.models import Blog
from django.contrib.sitemaps import Sitemap


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_on