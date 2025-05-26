from django.contrib import admin
from .models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorname', 'authorphone')

class BookAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'author', 'description','original_price', 'discount', 'final_price', 'pub_time')
# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)