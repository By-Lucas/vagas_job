# Generated by Django 4.1 on 2022-08-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidaturas", "0017_alter_quatidadecandidatura_vaga"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quatidadecandidatura",
            name="vaga",
            field=models.CharField(max_length=70),
        ),
    ]
