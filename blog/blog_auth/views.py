from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

# 如果需要使用 settings 中的 DEFAULT_FROM_EMAIL
from django.conf import settings

# 要使用 JsonResponse
from django.http.response import JsonResponse

# 產生數字 0-9
import string

# 隨機取樣
import random

# 引入 captcha model
from .models import CaptchaModel

# Create your views here.


def login(request):

    return render(request, "blog_auth/login.html")


def register(request):

    return render(request, "blog_auth/register.html")


def send_test_email(request):

    email = request.GET.get("email")

    if not email:
        return JsonResponse({"code": 400, "message": "請輸入正確的郵箱"})
    else:
        try:
            subject = "測試郵件主題"
            # ramdom.sample() 針對 0-9, 取6位數字變成陣列, 用 join() 拼接成字串
            captcha = "".join(random.sample(string.digits, 6))
            CaptchaModel.objects.update_or_create(email=email, defaults={'captcha':captcha})
            message = f"這是一封來自 Django 應用程式的測試郵件, 驗證碼為 {captcha}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return JsonResponse(
                {"code": 200, "message": "郵件發送成功", "number_code": captcha}
            )
        except Exception as e:
            return HttpResponse(f"郵件發送失敗: {e}")
