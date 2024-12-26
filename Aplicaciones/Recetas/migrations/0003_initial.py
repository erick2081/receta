# Generated by Django 5.1.3 on 2024-12-25 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Recetas', '0002_remove_ingrediente_receta_delete_comentario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tiempo_preparacion', models.PositiveIntegerField(help_text='Tiempo en minutos')),
                ('dificultad', models.CharField(choices=[('Fácil', 'Fácil'), ('Intermedio', 'Intermedio'), ('Difícil', 'Difícil')], max_length=50)),
                ('instrucciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.CharField(max_length=50)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='Recetas.receta')),
            ],
        ),
    ]