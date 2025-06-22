
from django.urls import path
from . import views

app_name = 'blog_auth'

urlpatterns = [ 
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('send_test_email', views.send_test_email, name='send_test_mail')
]