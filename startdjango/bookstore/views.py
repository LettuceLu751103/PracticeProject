from django.shortcuts import render, HttpResponse
from .models import Book, Author
from datetime import datetime

# Create your views here.

def index(request, tvno=0):
    tv_list = [
        {'name':'台視', 'tvcode':'xL0ch83RAK8'},
        {'name':'中視', 'tvcode':'jRItTbHImsQ'},
        {'name':'中視', 'tvcode':'wM0g8EoUZ_E'},
    ]
    tv = tv_list[tvno]
    username = 'Lettuce'
    now = datetime.now()
    context = {
        'username':username,
        'msg' : '歡迎來到生菜小館',
        'now' : now
    }
    # return render(request, 'bookstoreindex.html', context=context)
    return render(request, 'bookstoreindex.html', locals())

def getbooks(request):

    books = Book.objects.all()

    for b in books:

        print(b.bookname)
        print(b.author)
        print(b.pub_time)
        print(b.final_price)

    return HttpResponse(books)