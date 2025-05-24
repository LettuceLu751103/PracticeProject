from django.urls import path
from . import views

urlpatterns = [
    path('xyzindex/', views.xyzindex),
    path('static', views.static),
    path('bookindex', views.bookindex),
    path('add_book', views.add_book),
    path('query_book', views.query_book)
]
