# Generated by Django 5.0.3 on 2024-03-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0007_remove_tarea_orden_de_venta_tarea_tiempo_tarea_and_more'),
        ('procesos', '0003_remove_subproceso_proceso_subproceso_proceso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='subproceso',
        ),
        migrations.AddField(
            model_name='tarea',
            name='subproceso',
            field=models.ManyToManyField(related_name='tareas', to='procesos.subproceso'),
        ),
    ]
