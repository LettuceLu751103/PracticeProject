from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'blog_ntt/index.html')

def blog_detail(request):

    return render(request, 'blog_ntt/blog_detail.html')


def pub_blog(request):

    return render(request, 'blog_ntt/pub_blog.html')

