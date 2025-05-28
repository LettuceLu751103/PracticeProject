from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):

    return render(request, 'index.html')


def login(request):

    return render(request, 'login.html', locals())


# 註冊的視圖函數
@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        print(f'進來的請求為 POST 方法')

    else:
        print(f'進來的請求為 GET 方法')

        return render(request, 'register.html')
    return render(request, 'register.html')