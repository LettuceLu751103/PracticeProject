from django.shortcuts import render, HttpResponse
from blog_auth.models import UserModel
from django.views.decorators.http import require_http_methods
# Create your views here.
def index(request):
    
    print('===========================')
    print(request.session.get('user_id'))
    if request.session.get('user_id'):
        user_pk = request.session.get('user_id')
        loginuser = UserModel.objects.get(pk=user_pk)
        print(loginuser)
        email = loginuser.email
        username = loginuser.username
        print(f'email:{email}, username:{username}')
        
    print('===========================')
    
    return render(request, 'blog_ntt/index.html', locals())

def blog_detail(request):

    return render(request, 'blog_ntt/blog_detail.html')


def pub_blog(request):
    # 判斷是否登入
    if request.session.get('user_id'):
        user_pk = request.session.get('user_id')
        loginuser = UserModel.objects.get(pk=user_pk)
        print(loginuser)
        email = loginuser.email
        username = loginuser.username
        print(f'email:{email}, username:{username}')
        return render(request, 'blog_ntt/pub_blog.html', locals())
    
    else:
        print('當前沒有登入, 跳轉登入頁面')
        return render(request, 'blog_auth/login.html', locals())


@require_http_methods(['GET', 'POST'])
def blog_category_add(request):
    if request.method == "GET":
        # 判斷是否登入
        if request.session.get('user_id'):
            user_pk = request.session.get('user_id')
            loginuser = UserModel.objects.get(pk=user_pk)
            print(loginuser)
            email = loginuser.email
            username = loginuser.username
            userid = loginuser.pk
            print(f'email:{email}, username:{username}')
            return render(request, 'blog_ntt/blog_category_add.html', locals())
        
        else:
            print(f'尚未登入, 跳轉 loging 頁面')
            return render(request, 'blog_auth/login.html', locals())
    else:
        print('當前傳送 POST 請求, 解析傳進來的變數')

        print(request.POST)
        return HttpResponse('當前 post 請求')
