# Generated by Django 4.2.7 on 2023-12-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена (руб)'),
        ),
    ]
