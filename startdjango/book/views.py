from django.shortcuts import render, HttpResponse

# Create your views here.

def book_detail(request):
    bookinfo = request.GET.get('id')
    bookname = request.GET.get('name')
    return HttpResponse(f"圖書的號碼是:{bookinfo}, 圖書名稱是:{bookname}") 


# book_id 是設定在 url.py 裡面
def book_detail2(request, book_id):
    return HttpResponse(f"圖書的號碼是:{book_id}")