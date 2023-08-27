from django.urls import path
from django.contrib.auth import views as auth_view
from . import views


app_name = 'nguoidung'

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    path('login/' , auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='index.html'),name='logout'),
    path('profile/', views.profile, name= 'profile'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:postId>', views.getpost, name='post')
    
] 