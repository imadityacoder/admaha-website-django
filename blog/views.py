from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog,Category ,Contact, Comment
from django.contrib.auth.models import User
from .forms import AddForm,UpdateForm ,ContactForm,SignUpForm,CommentForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout , authenticate 
from .utils import send_admin_notification, send_user_notification


def home(request):
    posts=Blog.objects.all()
    data = {"posts":posts}
    return render(request,'blog/home.html',data)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your message is successfully submited!')
            return redirect('home')
        
        if not form.is_valid():
            messages.warning(request, f'Please, fill the form properly!')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})

    
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        related_posts = Blog.objects.filter(category=post.category).exclude(slug=post.slug)[:5]  # Adjust the filtering logic as needed
        context['related_posts'] = related_posts
        return context

class createpost(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog/createpost.html"
    form_class  = AddForm
    def form_valid(self, form):
        messages.success(self.request, f'Hurry, you created a new post.')
        form.instance.author = self.request.user
        return super().form_valid(form)

class updatepost(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/updatepost.html'
    form_class = UpdateForm
    def form_valid(self, form):
        messages.success(self.request, f'Hurry, you updated this post.')
        return super().form_valid(form)
    

class deletepost(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.warning(self.request, f'Successfully deleted!.')
        return super().form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request,'Congratulation,You are now a Admoha.com user !') 
            if user is not None:
                auth_login(request, user) 
                return redirect('home') 

    else:
        initial_data = {"username":'',"email":'',"password1":'',"password2":''}
        form = SignUpForm(initial = initial_data)
    return render(request, 'auth/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Weclome, back {request.user.username}')
            return redirect('home')
        else:
            messages.warning(request, f"Please enter right password and username!")

    else:
        initial_data = {"username":'',"password":''}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request,'Logout done !')
    return redirect('home')

@login_required
def userposts(request,username):
    try:
        user = User.objects.get(username=username)
        user_posts = Blog.objects.filter(author = user)
        data = {"user_posts":user_posts,
                "user":user}
    except:
        data ={"user":user}   
    return render(request,'auth/userposts.html',data)

def privacypolicy(request):
    return render(request,"blog/privacypolicy.html")

def terms_of_use(request):
    return render(request, 'blog/termsofuse.html')
