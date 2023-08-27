from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def getpost(request, postId):
    post = Post.objects.get(id = postId)
    posts = Post.objects.all()
    return render(request, 'post.html', {'post':post, 'posts':posts})

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Hi {username}, your account is created successfully!"
            )
            return redirect('nguoidung:index')
    else:
        form = UserRegisterForm()
        messages.error(
            request, "Sorry, there's something wrong with sytem. \nPlease try again in a few seconds."
        )
    return render(request, 'signup.html', {'form':form})

def profile(request):
   return render(request, 'profile.html')