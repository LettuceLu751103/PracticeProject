from django.urls import path
from . import views


urlpatterns = [
    # 首頁
    path('index/', views.index),
    path('<int:tvno>/', views.index),
    path('getbooks/', views.getbooks)
]