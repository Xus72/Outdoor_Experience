# Generated by Django 3.0.3 on 2020-09-22 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200916_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'permissions': (('add_activ', 'Añadir actividad'), ('edit_activ', 'Editar proveedor'), ('rem_activ', 'Eliminar actividad'))},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'permissions': (('add_prov', 'Añadir proveedor'), ('edit_prov', 'Editar proveedor'), ('rem_prov', 'Eliminar proveedor'))},
        ),
    ]
