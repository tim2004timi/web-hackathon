# Generated by Django 4.2.7 on 2023-11-24 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillmentapp', '0006_alter_operator_user_alter_product_numbers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='qr',
        ),
        migrations.AddField(
            model_name='delivery',
            name='barcode',
            field=models.ImageField(blank=True, default=None, upload_to='', verbose_name='Штрих-код'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default=None, max_length=30, verbose_name='Размер (20*20*30)'),
        ),
    ]