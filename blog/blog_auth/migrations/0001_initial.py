# Generated by Django 5.0.3 on 2025-06-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('captcha', models.CharField(max_length=6)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
