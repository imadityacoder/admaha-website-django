
from .models import Category

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def display_user(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return {'username': username}
