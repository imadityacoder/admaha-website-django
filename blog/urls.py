from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.detailview, name='detailview'),
    path('create/', views.create, name='create'),
    path('<slug:slug>/delete/', views.delete, name='delete'),
    path('<slug:slug>/update/', views.update, name='update'),

]