from django.db import models
from blog_auth.models import UserModel

# Create your models here.

class BlogCategory(models.Model):
    category= models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)


