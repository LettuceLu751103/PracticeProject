from django.shortcuts import render, HttpResponse

# Create your views here.

def movie_list(request):
    return HttpResponse(f"電影詳細清單")

def movie_detail(request, id):
    return HttpResponse(f"電影 id:{id}")