# Generated by Django 3.2.15 on 2022-08-12 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20220811_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='escolaridade',
            name='outros',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
    ]
