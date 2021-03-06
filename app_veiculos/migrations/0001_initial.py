# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaDoVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Ex. Nissan, Honda, fiat', max_length=20, verbose_name='Marca do veiculo')),
            ],
            options={
                'verbose_name': 'Marca do Veiculo',
                'ordering': ('marca',),
                'verbose_name_plural': 'Marca Dos Veiculos',
            },
        ),
        migrations.CreateModel(
            name='TiposDeVeiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo de Veiculos')),
            ],
            options={
                'verbose_name': 'tipo de veiculo',
                'ordering': ('tipo',),
                'verbose_name_plural': 'Tipo de veiculos',
            },
        ),
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('cor', models.CharField(max_length=10, verbose_name='Cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_veiculos.MarcaDoVeiculo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_veiculos.TiposDeVeiculos')),
            ],
            options={
                'verbose_name': 'Veiculo',
                'ordering': ('tipo', 'marca', 'modelo'),
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
