from django.db import models
import bcrypt

# Create your models here.
class CaptchaModel(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=6)
    created_time = models.DateTimeField(auto_now_add=True)

# username = request.POST.get('username')
# email = request.POST.get('email')
# password = request.POST.get('password')
# confirm = request.POST.get('confirm')
# code = request.POST.get('code')

class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

