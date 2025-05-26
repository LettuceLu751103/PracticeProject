from django.db import models

# Create your models here.


class Author(models.Model):
    authorname = models.CharField(max_length=200)
    authorphone = models.CharField(max_length=14)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.authorname
    
class Book(models.Model):
    bookname = models.CharField(max_length=200, default='未命名書籍')
    original_price = models.IntegerField()
    discount = models.FloatField()
    final_price = models.IntegerField()
    pub_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.bookname

