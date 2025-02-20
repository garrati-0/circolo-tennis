# Generated by Django 4.2.6 on 2024-02-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='immagine',
        ),
        migrations.AddField(
            model_name='product',
            name='imagine',
            field=models.ImageField(blank=True, null=True, upload_to='prodotti\\static\\img'),
        ),
        migrations.AddField(
            model_name='product',
            name='nomeimg',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
