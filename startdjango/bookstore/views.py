from django.shortcuts import render, HttpResponse
from .models import Book, Author


# Create your views here.

def index(request):

    return HttpResponse('這是bookstore首頁')

def getbooks(request):

    books = Book.objects.all()

    print(books)

    return HttpResponse('成功抓取圖書資訊')