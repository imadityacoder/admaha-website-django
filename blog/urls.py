from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('<str:user>/posts/',views.userposts,name="userposts"),

    path('category/<str:cat>/', views.category, name='category'),
    path('create/', views.createpost.as_view(), name='createpost'),
    path('<slug:slug>/', views.detailview.as_view(), name='detailview'),
    path('<slug:slug>/delete/', views.deletepost.as_view(), name='deletepost'),
    path('<slug:slug>/update/', views.updatepost.as_view(), name='updatepost'),

]