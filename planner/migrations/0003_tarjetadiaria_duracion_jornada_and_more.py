# Generated by Django 5.0.3 on 2024-03-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_tarjetadiaria_tareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjetadiaria',
            name='duracion_jornada',
            field=models.IntegerField(choices=[(8, '8 horas'), (12, '12 horas')], default=8),
        ),
        migrations.AddField(
            model_name='tarjetadiaria',
            name='total_minutos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]