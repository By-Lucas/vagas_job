# Generated by Django 3.2.15 on 2022-08-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0012_auto_20220817_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='requisitos_adicionais',
            field=models.ManyToManyField(blank=True, null=True, to='vagas.RequisitosVaga'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='status',
            field=models.BooleanField(blank=True, default=True, help_text='Vaga ativa / inativa', null=True),
        ),
    ]