# Generated by Django 5.0.3 on 2024-03-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0002_remove_proceso_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subproceso',
            name='proceso',
        ),
        migrations.AddField(
            model_name='subproceso',
            name='proceso',
            field=models.ManyToManyField(related_name='subprocesos', to='procesos.proceso'),
        ),
    ]
