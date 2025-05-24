"""
URL configuration for startdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book import views as bookview
from home import views as homeview
urlpatterns = [
    path('admin/', admin.site.urls),
    # get 傳送參數方法 1, 傳統傳參
    path('bookinfo/', bookview.book_detail),
    # get 傳送參數方法 2, 直接接在URL後方
    path('bookinfo2/<int:book_id>', bookview.book_detail2),

    path('movie/', include('movie.urls')),
    path('', homeview.index),
    path('baidu', homeview.baidu),
    path('bookinfo3/', homeview.bookinfo),

    path('xyzindex/', bookview.xyzindex),

    path('static', bookview.static),
    path('bookindex', bookview.bookindex),
    path('add_book', bookview.add_book)
]
