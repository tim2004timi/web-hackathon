# Generated by Django 4.2.7 on 2023-11-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillmentapp', '0012_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('В пути до нас', 'В пути до нас'), ('Ожидает заявку на отгрузку', 'Ожидает заявку на отгрузку'), ('В процессе подтверждения', 'В процессе подтверждения'), ('Ожидает штрихкод для тары', 'Ожидает штрихкод для тары'), ('Отгружено, ожидает оплаты', 'Отгружено, ожидает оплаты'), ('Оплата подтверждена', 'Оплата подтверждена')], default='В пути до нас', max_length=40, verbose_name='Статус'),
        ),
    ]