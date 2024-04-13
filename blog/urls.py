from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('category/<str:cat>/', views.category, name='category'),
    path('create/', views.createpost.as_view(), name='createpost'),
    path('<slug:slug>/', views.detailview.as_view(), name='detailview'),
    path('<slug:slug>/delete/', views.deletepost.as_view(), name='deletepost'),
    path('<slug:slug>/update/', views.updatepost.as_view(), name='updatepost'),

]