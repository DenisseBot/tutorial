# Generated by Django 3.2.4 on 2021-07-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='especialidad',
            field=models.CharField(default=1, max_length=20, verbose_name='especialidad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='sucursal',
            field=models.CharField(default=2, max_length=50, verbose_name='sucursal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='etapa',
            field=models.IntegerField(blank=True, choices=[(1, 'Primera'), (2, 'Segunda'), (3, 'Tercera')], default=None, verbose_name='Etapa'),
        ),
    ]