from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def baidu(request):
    return render(request, 'baidu.html')