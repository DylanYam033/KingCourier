# Generated by Django 4.1 on 2023-06-04 22:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0005_alter_detalleestadopedido_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]