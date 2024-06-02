from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacypolicy, name='privacypolicy'),
    path('terms-of-use/', views.terms_of_use, name='termsofuse'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/posts/',views.userposts,name="userposts"),
    path('sitemap.xml', views.sitemap, name='sitemap'),

    path('category/<str:cat>/', views.category, name='category'),
    path('create/', views.createpost.as_view(), name='createpost'),
    path('<slug:slug>/', views.detailview.as_view(), name='detailview'),
    path('<slug:slug>/delete/', views.deletepost.as_view(), name='deletepost'),
    path('<slug:slug>/update/', views.updatepost.as_view(), name='updatepost'),

]
