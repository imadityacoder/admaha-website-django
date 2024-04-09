from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,DetailView
from .models import Blog,Category
from .forms import AddForm,UpdateForm
from django.urls import reverse_lazy


categories = Category.objects.all()
cat_data = {"categories":categories,}
# Create your views here.
def home(request):
    posts = Blog.objects.all()
    data = {"posts":posts,"categories":categories,}
     
    return render(request,'blog/home.html',data)

def about(request):
    return render(request,'blog/about.html',cat_data)

def contact(request):
    return render(request,'blog/contact.html',cat_data)

def category(request,cat):
    category_posts = Blog.objects.filter(category=cat)
    data = {"category_posts":category_posts}
    return render(request,'blog/category.html',data)
    

class detailview(DetailView):
    model = Blog
    template_name = "blog/detailview.html"
    slug_url_kwarg = 'slug'

class createpost(CreateView):
    model = Blog
    template_name = "blog/createpost.html"
    form_class  = AddForm

class updatepost(UpdateView):
    model = Blog
    template_name = 'blog/updatepost.html'
    form_class = UpdateForm

class deletepost(DeleteView):
    model = Blog
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('bloghome')
