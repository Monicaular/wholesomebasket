# Generated by Django 4.2.13 on 2024-07-28 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0003_carouselitem_text_link_carouselitem_title_link"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CarouselItem",
        ),
    ]
