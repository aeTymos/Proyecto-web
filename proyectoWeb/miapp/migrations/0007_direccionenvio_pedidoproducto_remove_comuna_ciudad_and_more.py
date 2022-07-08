# Generated by Django 4.0.6 on 2022-07-08 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miapp', '0006_alter_producto_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('fecha_agregado', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_agregado', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comuna',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='detallepedido',
            name='id_pedido',
        ),
        migrations.RemoveField(
            model_name='detallepedido',
            name='producto_id_producto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='correo_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='direccion_envio',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='direccion_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='estado_pedido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='dir_envio_default',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fono_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='pass_usuario',
        ),
        migrations.AddField(
            model_name='pedido',
            name='completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_transaccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='miapp.usuario'),
        ),
        migrations.DeleteModel(
            name='Ciudad',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='DetallePedido',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='miapp.pedido'),
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='miapp.producto'),
        ),
        migrations.AddField(
            model_name='direccionenvio',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='miapp.pedido'),
        ),
        migrations.AddField(
            model_name='direccionenvio',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='miapp.usuario'),
        ),
    ]
