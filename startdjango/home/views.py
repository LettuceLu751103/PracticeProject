from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def baidu(request):
    return render(request, 'baidu.html')


def bookinfo(request):
    #1 字典類型
    book = {'id':'01', 'name':'西遊記'}
    #2 變量類型
    author = '羅貫中'
    #3 列表類型
    books = [
        {'id':'02', 'name':'西遊記', 'author' : '羅貫中'},
        {'id':'03', 'name':'東遊記', 'author' : '東貫中'},
        {'id':'04', 'name':'北遊記', 'author' : '北貫中'},
        {'id':'05', 'name':'南遊記', 'author' : '南貫中'}
    ]
    return render(request, 'bookinfo.html', context={'author': author, 'book': book, 'books':books})
