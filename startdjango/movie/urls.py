from django.urls import path
from . import views

urlpatterns = [
    path('list', views.movie_list, name="movie_list"),
    path('detail/<int:id>', views.movie_detail, name="movie_detail")
]