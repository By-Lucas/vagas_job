# Generated by Django 3.2.15 on 2022-08-13 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidaturas', '0010_auto_20220812_2135'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EscolaridadeVaga',
            new_name='EscolaridadeCandidatura',
        ),
        migrations.RenameModel(
            old_name='RequisitosVaga',
            new_name='RequisitosCandidatura',
        ),
    ]
