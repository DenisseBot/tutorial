# Generated by Django 3.2.4 on 2021-07-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_usuario_etapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='etapa',
            field=models.IntegerField(blank=True, choices=[(0, 'Sin etapa'), (1, 'Primera'), (2, 'Segunda'), (3, 'Tercera')], default=0, null=True, verbose_name='Etapa'),
        ),
    ]
