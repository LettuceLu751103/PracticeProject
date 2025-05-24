from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('baidu', views.baidu),
    path('bookinfo3/', views.bookinfo),
]