from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
# 如果需要使用 settings 中的 DEFAULT_FROM_EMAIL
from django.conf import settings 

# Create your views here.

def login(request):

    return render(request, 'blog_auth/login.html')

def register(request):

    return render(request, 'blog_auth/register.html')


def send_test_email(request):
    subject = '測試郵件主題'
    message = '這是一封來自 Django 應用程式的測試郵件'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['boneebtc@protonmail.com']

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse('郵件發送成功!')
    except Exception as e:
        return HttpResponse(f"郵件發送失敗: {e}")