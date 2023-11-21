# Generated by Django 4.2.7 on 2023-11-20 19:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('article', models.IntegerField(default=10001, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(10000)])),
                ('name', models.CharField(default=None, max_length=30)),
                ('size', models.CharField(default=None, max_length=30)),
                ('color', models.CharField(default=None, max_length=30)),
                ('numbers', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)])),
                ('status', models.CharField(blank=True, default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, default=None, max_length=254)),
                ('telegram', models.CharField(blank=True, default=None, max_length=30)),
                ('time_signup', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fulfillmentapp.product')),
                ('address', models.TextField()),
                ('driver_fio', models.CharField(max_length=50)),
                ('car_number', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('qr', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fulfillmentapp.seller'),
        ),
    ]
