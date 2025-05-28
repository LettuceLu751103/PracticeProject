from django.urls import path
from . import views as mysiteviews

urlpatterns = [
    path('', mysiteviews.index),
    path('login', mysiteviews.login, name='login'),
    path('register', mysiteviews.register)
]