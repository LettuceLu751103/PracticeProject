from django.urls import path
from . import views

urlpatterns = [
    path('xyzindex/', views.xyzindex),
    path('static', views.static),
    path('bookindex', views.bookindex),
    path('add_book', views.add_book),
    path('query_book', views.query_book),
    # get 傳送參數方法 1, 傳統傳參
    path('bookinfo/', views.book_detail),
    # get 傳送參數方法 2, 直接接在URL後方
    path('bookinfo2/<int:book_id>', views.book_detail2),
]
