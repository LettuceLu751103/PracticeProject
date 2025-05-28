from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
# 引入 model class
from .models import Userinfo
# 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# hash 密碼
from django.contrib.auth.hashers import make_password

# Create your views here.

# 首頁頁面的視圖函數
def index(request):
    return render(request, "index.html")

# 登入頁面的視圖函數
def login(request):
    return render(request, "login.html", locals())


# 註冊的視圖函數
@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        print(f"進來的請求為 POST 方法")
        email = request.POST.get("email", "").strip()
        nickname = request.POST.get("nickname", "").strip()
        password = request.POST.get("password", "")
        confirm_pw = request.POST.get("confirm_pw", "")
        print(f"{email} {nickname} {password} {confirm_pw}")

        # 判斷進來的資料有沒有為空的
        if not email or not nickname or not password or not confirm_pw:
            context = {
                "email": email,
                "nickname": nickname,
                "password": password,
                "confirm_pw": confirm_pw,
                "message": "所有欄位都必須填寫",
            }
            return render(request, "register.html", context=context)
        
        # 密碼一致性
        if password != confirm_pw:
            context = {
                "email": email,
                "nickname": nickname,
                "password": password,
                "confirm_pw": confirm_pw,
                "message": "密碼不一致",
            }
            return render(request, "register.html", context=context)
        
        # 驗證 email 格式
        try:
            validate_email(email)
        except ValidationError:
            context = {
                "email": email,
                "nickname": nickname,
                "password": password,
                "confirm_pw": confirm_pw,
                "message": "請輸入正確格式的 Email",
            }
            return render(request, "register.html", context=context)

        # email 是否在 db 中存在(查詢 Userinfo 表)
        query_result = Userinfo.objects.filter(email=email).exists()
        if query_result:
            context = {
                "email": email,
                "nickname": nickname,
                "password": password,
                "confirm_pw": confirm_pw,
                "message": "email 已存在",
            }
            return render(request, "register.html", context=context)
        # 基本驗證成功, 儲存帳號到 db
        else:
        # Userinfo 表中沒有該 email, 存入 db 並跳轉 login 頁面

            Userinfo.objects.create(email=email, nickname=nickname, password=make_password(password))

            return redirect('login')
    else:
        print(f"進來的請求為 GET 方法")
        return render(request, "register.html")
