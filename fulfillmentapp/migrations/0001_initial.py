# Generated by Django 4.2.7 on 2023-12-10 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(blank=True, default=None, max_length=30, verbose_name='Телеграм')),
                ('telegram_chat_id', models.CharField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Ассистент',
                'verbose_name_plural': 'Ассистенты (колл-центр)',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('driver_fio', models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО водителя')),
                ('car_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер авто')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('label', models.FileField(blank=True, default=None, null=True, upload_to='labels/', verbose_name='Этикетка')),
                ('marketplace_barcode', models.FileField(null=True, upload_to='marketplace_barcodes/', verbose_name='Штрих-код для маркетплейса')),
                ('wrapper_barcode', models.FileField(blank=True, default=None, null=True, upload_to='wrapper_barcodes/', verbose_name='Штрих-код для тары')),
                ('bill', models.FileField(blank=True, default=None, null=True, upload_to='bills/', verbose_name='Счет')),
            ],
            options={
                'verbose_name': 'Отгрузка',
                'verbose_name_plural': 'Отгрузки',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, verbose_name='Почта')),
                ('telegram', models.CharField(blank=True, default=None, max_length=30, verbose_name='Телеграм')),
                ('telegram_chat_id', models.CharField(blank=True, default='')),
                ('time_signup', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(default=None, max_length=30, verbose_name='Артикул маркетплейса')),
                ('name', models.CharField(default=None, max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/photo', verbose_name='Фото товара')),
                ('size', models.CharField(default=None, max_length=30, verbose_name='Размер (20*20*30)')),
                ('weight', models.IntegerField(default=1, verbose_name='Вес (кг)')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_types', to='fulfillmentapp.seller', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Тип товара',
                'verbose_name_plural': 'Типы товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('В пути до нас', 'В пути до нас'), ('Ожидает заявку на отгрузку', 'Ожидает заявку на отгрузку'), ('В процессе подтверждения', 'В процессе подтверждения'), ('Ожидает штрихкод для тары', 'Ожидает штрихкод для тары'), ('Отгружено, ожидает оплаты', 'Отгружено, ожидает оплаты'), ('Оплата подтверждена', 'Оплата подтверждена')], default='В пути до нас', max_length=40, verbose_name='Статус')),
                ('delivery', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='fulfillmentapp.delivery', verbose_name='Отгрузка')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='fulfillmentapp.producttype', verbose_name='Тип товара')),
                ('seller', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='fulfillmentapp.seller', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Почта')),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оператор',
                'verbose_name_plural': 'Операторы склада',
            },
        ),
        migrations.AddField(
            model_name='delivery',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='fulfillmentapp.producttype', verbose_name='Тип товара'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='seller',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='fulfillmentapp.seller', verbose_name='Продавец'),
        ),
    ]
