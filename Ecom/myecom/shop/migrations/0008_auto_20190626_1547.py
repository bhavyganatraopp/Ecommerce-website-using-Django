# Generated by Django 2.2.1 on 2019-06-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discreption',
            field=models.CharField(max_length=300000),
        ),
    ]
