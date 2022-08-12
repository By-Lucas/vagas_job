# Generated by Django 3.2.15 on 2022-08-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0005_vagas_tipo'),
        ('candidaturas', '0005_auto_20220812_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatura',
            name='vaga',
        ),
        migrations.AddField(
            model_name='candidatura',
            name='vaga',
            field=models.ManyToManyField(to='vagas.Vagas'),
        ),
    ]
