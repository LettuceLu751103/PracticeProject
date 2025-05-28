from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html')


def login(request):

    return render(request, 'login.html', locals())


# 註冊的視圖函數
def register(request):

    return render(request, 'register.html')