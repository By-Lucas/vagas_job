# Generated by Django 4.1 on 2022-08-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidaturas", "0025_alter_quatidadecandidatura_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quatidadecandidatura",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
