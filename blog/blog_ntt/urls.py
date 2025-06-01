from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog_ntt'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.blog_detail, name='blog_detail')
]