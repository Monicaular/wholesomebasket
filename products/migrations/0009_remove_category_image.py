# Generated by Django 4.2.13 on 2024-07-13 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_remove_product_fixed_size_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="image",
        ),
    ]
