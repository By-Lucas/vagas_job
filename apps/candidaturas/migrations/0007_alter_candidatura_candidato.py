# Generated by Django 3.2.15 on 2022-08-12 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidaturas', '0006_auto_20220812_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatura',
            name='candidato',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
