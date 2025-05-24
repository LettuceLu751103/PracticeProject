from django.shortcuts import render, HttpResponse

# 使用 django 封裝好的 connection 對象, 會自動讀取 settings.py 中數據庫的配置訊息
from django.db import connection

# 導入 Book model
from .models import Book

# Create your views here.

def book_detail(request):
    bookinfo = request.GET.get('id')
    bookname = request.GET.get('name')
    return HttpResponse(f"圖書的號碼是:{bookinfo}, 圖書名稱是:{bookname}") 


# book_id 是設定在 url.py 裡面
def book_detail2(request, book_id):
    return HttpResponse(f"圖書的號碼是:{book_id}")


def xyzindex(request):
    print(f"進到 book app 的 views.py")
    context = {
        'articles': [
            'ChatGPT5 發佈',
            'Django 5 發佈',
            'Html 5 發佈',
            '模板繼承'
        ]
    }
    return render(request, 'xyz_index.html', context=context)

def static(request):
    return render(request, 'static.html')

def bookindex(request):
    # 獲取游標對象
    cursor = connection.cursor()
    # 拿到游標對象後執行sql語句
    cursor.execute("select * from book")
    # 獲取所有數據
    rows = cursor.fetchall()
    # 遍歷查詢到的數據
    for row in rows:
        print(row)
    
    return HttpResponse('連接 mysql, 查找數據成功!!!')

def add_book(request):
    book = Book(name='三國演義', author='羅貫中', price='230.0')
    print(book.name, book.author, book.price)
    book.save()
    return HttpResponse('圖書插入成功')


