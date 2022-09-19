from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all().filter(published=True).order_by('-created_date')
    recent_post = Post.objects.filter(published=True).order_by('-id')[0:3]
    ctx = {
        'posts':posts,
        'recent':recent_post,
    }
    return render(request, 'home.html',ctx)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('post_list')
