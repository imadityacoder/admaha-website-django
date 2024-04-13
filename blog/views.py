from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
from .models import Blog,Category #,Contact
from .forms import AddForm,UpdateForm #,ContactForm
from admoha_website import settings
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

# def contact(request):
#     sub = ContactForm()
#     if request.method == 'POST':
#         sub = ContactForm(request.POST)
#         if sub.is_valid():
#             sub.save()
#             return render(request, 'blog/home.html')
#     return render(request, 'blog/contact.html', {'form': sub})
    
def category(request,cat):
    category_posts = Blog.objects.filter(category=Category.objects.get(name=cat))
    data = {"category_posts":category_posts,
            "cat":cat}
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
    success_url = reverse_lazy('home')
