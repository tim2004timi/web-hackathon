# Generated by Django 4.2.7 on 2023-11-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillmentapp', '0010_alter_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='barcode',
        ),
        migrations.AddField(
            model_name='delivery',
            name='bill',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='Счет'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='label',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='Этикетка'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='marketplace_barcode',
            field=models.ImageField(null=True, upload_to='', verbose_name='Штрих-код для маркетплейса'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='wrapper_barcode',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Штрих-код для тары'),
        ),
    ]
