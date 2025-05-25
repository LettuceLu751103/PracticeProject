from django.urls import path
from . import views


urlpatterns = [
    # 首頁
    path('', views.index),
    path('getbooks/', views.getbooks)
]