# Generated by Django 4.2 on 2024-07-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
    ]
