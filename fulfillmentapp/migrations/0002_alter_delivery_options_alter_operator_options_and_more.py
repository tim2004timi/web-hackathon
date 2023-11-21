# Generated by Django 4.2.7 on 2023-11-20 20:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Отгрузка', 'verbose_name_plural': 'Отгрузки'},
        ),
        migrations.AlterModelOptions(
            name='operator',
            options={'verbose_name': 'Оператор', 'verbose_name_plural': 'Операторы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Продавец', 'verbose_name_plural': 'Продавцы'},
        ),
        migrations.AlterField(
            model_name='delivery',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='car_number',
            field=models.CharField(max_length=20, verbose_name='Номер авто'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='driver_fio',
            field=models.CharField(max_length=50, verbose_name='ФИО водителя'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fulfillmentapp.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='qr',
            field=models.ImageField(upload_to='', verbose_name='QR'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='login',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='password',
            field=models.CharField(max_length=20, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Артикль'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default=None, max_length=30, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='numbers',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Кол-во'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fulfillmentapp.seller', verbose_name='Продавец'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default=None, max_length=30, verbose_name='Размер (20х20х30)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='login',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='password',
            field=models.CharField(max_length=20, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='telegram',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Телеграм'),
        ),
    ]
