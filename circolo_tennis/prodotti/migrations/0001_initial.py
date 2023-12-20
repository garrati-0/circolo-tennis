# Generated by Django 4.2.6 on 2023-12-20 14:53

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
            name='Recensione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testo', models.TextField()),
                ('voto', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodotto', models.CharField(max_length=255)),
                ('prezzo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=255)),
                ('immagine', models.CharField(default='recchette.jpeg', max_length=254)),
                ('quantita', models.PositiveIntegerField(default=0)),
                ('recensioni', models.ManyToManyField(blank=True, related_name='recensioni_prodotto', to='prodotti.recensione')),
            ],
        ),
        migrations.CreateModel(
            name='Preferiti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodotti.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
