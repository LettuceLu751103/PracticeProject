from django.urls import path
from . import views as mysiteviews

urlpatterns = [
    path('', mysiteviews.index),
    path('login', mysiteviews.login),
    path('register', mysiteviews.register)
]