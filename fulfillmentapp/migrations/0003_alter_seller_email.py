# Generated by Django 4.2.7 on 2023-11-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillmentapp', '0002_alter_seller_telegram_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
    ]