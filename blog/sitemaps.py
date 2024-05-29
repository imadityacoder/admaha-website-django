from blog.models import Blog
from django.contrib.sitemaps import Sitemap


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_on
