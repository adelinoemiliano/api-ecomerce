# Generated by Django 5.1.3 on 2025-01-11 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '__first__'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('completo', models.BooleanField(default=False)),
                ('transacao_id', models.CharField(max_length=100, unique=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='pedidos.pedido')),
            ],
        ),
    ]
