# Generated by Django 4.2 on 2024-07-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_telegram_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_chat_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram chat'),
        ),
    ]
