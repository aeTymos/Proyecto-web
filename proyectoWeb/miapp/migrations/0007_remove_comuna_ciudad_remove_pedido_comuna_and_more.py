# Generated by Django 4.0.6 on 2022-07-06 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0006_alter_producto_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='comuna',
        ),
        migrations.DeleteModel(
            name='Ciudad',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
