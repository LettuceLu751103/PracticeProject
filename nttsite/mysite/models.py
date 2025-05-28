from django.db import models

# Create your models here.
class Userinfo(models.Model):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nickname} ({self.email})"