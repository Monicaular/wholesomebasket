# Generated by Django 4.2.13 on 2024-07-26 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_price_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]