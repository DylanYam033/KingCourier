# Generated by Django 4.1 on 2023-04-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionClientes', '0005_cliente_activo_sucursale_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='identificacion',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
