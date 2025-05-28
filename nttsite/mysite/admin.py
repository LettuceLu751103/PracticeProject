from django.contrib import admin
from .models import Userinfo


# way 1
@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ("email", "nickname", "password", "created_time")

# way 2
# Register your models here.
# ex: admin.site.register(model class)
# admin.site.register(Userinfo)