# Generated by Django 4.2.6 on 2024-02-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0003_product_descrizione_product_informazioni'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferiti',
            name='counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
