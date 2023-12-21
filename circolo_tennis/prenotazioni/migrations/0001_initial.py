# Generated by Django 4.2.6 on 2023-12-20 16:54

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
            name='PrenotazioneCampo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(choices=[('Campo 1', 'Campo 1'), ('Campo 2', 'Campo 2'), ('Campo 3', 'Campo 3')], max_length=10)),
                ('orario', models.TimeField()),
                ('data', models.DateField()),
                ('settimana', models.IntegerField()),
                ('prenotato', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
