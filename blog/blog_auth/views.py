from django.shortcuts import render

# Create your views here.

def login(request):

    return render(request, 'blog_auth/login.html')

def register(request):

    return render(request, 'blog_auth/register.html')