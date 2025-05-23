# Generated by Django 5.0.3 on 2025-05-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
