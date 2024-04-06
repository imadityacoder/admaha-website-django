from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def detailview(request,slug):
    return render(request,'blog/detailview.html')

def create(request,slug):
    return render(request,'blog/createpost.html')

def update(request,slug):
    return render(request,'blog/updatepost.html')

def delete(request,slug):
    return render(request,'blog/deletepost.html')
