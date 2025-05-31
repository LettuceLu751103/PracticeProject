from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog_ntt'

urlpatterns = [
    path('', views.index, name='index'),
]