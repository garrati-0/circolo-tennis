# Generated by Django 4.2.6 on 2024-02-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0002_remove_product_immagine_product_imagine_and_more'),
        ('carrelo', '0002_alter_ordineeffettuato_id_indirizzo_delete_indirizzo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordineeffettuato',
            name='id_prodotto',
        ),
        migrations.AddField(
            model_name='ordineeffettuato',
            name='id_prodotto',
            field=models.ManyToManyField(to='prodotti.product'),
        ),
    ]
