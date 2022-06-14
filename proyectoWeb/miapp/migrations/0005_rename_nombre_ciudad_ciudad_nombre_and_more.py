# Generated by Django 4.0.4 on 2022-06-11 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='nombre_ciudad',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='region_id_region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='comuna',
            old_name='ciudad_id_ciudad',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='comuna',
            old_name='nombre_comuna',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='detallepedido',
            old_name='pedido_id_pedido',
            new_name='id_pedido',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='id_comuna',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='descrip_producto',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_producto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio_producto',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='stock_producto',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='id_tiproducto',
            new_name='tipo_de_producto',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='nombre_region',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='descrip_tiproducto',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='nombre_tiproducto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='comuna_id_comuna',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='correo_usuario',
            new_name='correo',
        ),
    ]
