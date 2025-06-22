from django.shortcuts import render
from blog_auth.models import UserModel

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

    return render(request, 'blog_ntt/pub_blog.html')

