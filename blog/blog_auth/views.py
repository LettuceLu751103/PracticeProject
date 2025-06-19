from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.urls import reverse
# 如果需要使用 settings 中的 DEFAULT_FROM_EMAIL
from django.conf import settings
from .models import UserModel

# 要使用 JsonResponse
from django.http.response import JsonResponse

# 產生數字 0-9
import string

# 隨機取樣
import random

# 引入 captcha model
from .models import CaptchaModel

# 引入http方法裝飾器
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'GET':
        print(f'Get 請求, 傳送 login 模板')
        return render(request, "blog_auth/login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        print(f'email:{email}, password:{password}')
        try:
            user = UserModel.objects.get(email=email)
            print(user.email)
            print(user.password)
            print(remember)
            if user.check_password(password):
                print(f'使用者登入成功')
                return redirect('/blog')
            else:
                message = '密碼錯誤!!!'
                return render(request, "blog_auth/login.html", locals())
        except UserModel.DoesNotExist:
            message = '郵箱或密碼錯誤!!!'
            return render(request, "blog_auth/login.html", locals())
        
@require_http_methods(['GET','POST'])
def register(request):
    print(request.method)
    if request.method == 'GET':
        print('get 請求')
        return render(request, "blog_auth/register.html")
    else:
        print('post 請求')
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        code = request.POST.get('code')
        print(f'{username}, {email}, {password}, {confirm}, {code}')
        # 先用POST進來的email, 查找出來的物件 captcha 比對 POST 進來的驗證碼, 成功就往下繼續驗證, 反之將原先的資訊返回
        code_and_email_in_DB = CaptchaModel.objects.get(email = email)
        if code_and_email_in_DB.captcha == code:
            print(f'POST進來的驗證碼跟DB中的captcha相同')
            #1 驗證碼比對成功, 繼續比對 user table 當中是否有相同的 email
            exist = UserModel.objects.filter(email=email).exists()
            if exist:
                message = '郵箱已存在!!!'
                return render(request, "blog_auth/register.html", {'username':username, 'email':email, 'password':password, 'confirm':confirm, 'code':code, 'message':message})
            # 在查找 user 表, 比對有沒有重複的 email, 若有, 則不註冊, 攜帶原先參數回到 register 頁面
            else:
                new_user = UserModel(username=username, email=email)
                new_user.set_password(password)
                new_user.save()
            # 若沒有, 則註冊, redirect 到 login 頁面
            return redirect('/auth/login')
        else:
            #1 驗證碼比對失敗, 將原先 POST 進來的資料返回給 register.html
            message = '驗證碼不相符, 請重新獲取'
            return render(request, "blog_auth/register.html", {'username':username, 'email':email, 'password':password, 'confirm':confirm, 'code':code, 'message':message})
        
        
        


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
