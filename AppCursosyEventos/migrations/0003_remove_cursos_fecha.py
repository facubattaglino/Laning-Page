# Generated by Django 4.0.5 on 2022-06-21 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCursosyEventos', '0002_cursos_fecha_eventos_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='fecha',
        ),
    ]
