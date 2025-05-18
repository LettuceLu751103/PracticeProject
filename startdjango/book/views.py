from django.shortcuts import render, HttpResponse

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