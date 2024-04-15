from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog,Category #,Contact
from .forms import AddForm,UpdateForm #,ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

categories = Category.objects.all()
cat_data = {"categories":categories}

def home(request):
    posts = Blog.objects.all()
    data = {"posts":posts,
            "categories":categories,
            }
    return render(request,'blog/home.html',data)

def about(request):
    return render(request,'blog/about.html',cat_data)

def contact(request):
    return render(request, 'blog/contact.html'.cat_data)
    
def category(request,cat):
    try:
        category_posts = Blog.objects.filter(category=Category.objects.get(name=cat))
        data = {"category_posts":category_posts,
                "cat":cat}
    except:
        data ={"cat":cat}   
    return render(request,'blog/category.html',data)
    

class detailview(DetailView):
    model = Blog
    template_name = "blog/detailview.html"
    slug_url_kwarg = 'slug'


class createpost(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog/createpost.html"
    form_class  = AddForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class updatepost(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/updatepost.html'
    form_class = UpdateForm


class deletepost(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        initial_data = {"username":'',"password1":'',"password2":''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/signup.html', {'form': form})

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # redirect to home page or wherever you want
    else:
        initial_data = {"username":'',"password":''}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def userposts(request,user):
    try:
        user_posts = Blog.objects.filter(user = request.user)
        data = {"user_posts":user_posts,
                "user":user}
    except:
        data ={"user":user}   
    return render(request,'blog/userposts.html',data)
