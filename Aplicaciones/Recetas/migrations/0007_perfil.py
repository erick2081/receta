# Generated by Django 5.1.3 on 2025-01-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recetas', '0006_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('idioma', models.CharField(max_length=50)),
                ('fecha_caducidad', models.DateField()),
                ('creador', models.CharField(max_length=255)),
            ],
        ),
    ]
