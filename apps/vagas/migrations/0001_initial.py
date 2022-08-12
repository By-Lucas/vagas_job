# Generated by Django 3.2.15 on 2022-08-12 01:06

from django.db import migrations, models
import django.utils.timezone
import vagas.models.models_vagas


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EscolaridadeVaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequisitosVaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_por', models.CharField(max_length=50)),
                ('codigo', models.CharField(blank=True, default=vagas.models.models_vagas.gerar_codigo, editable=False, max_length=14, null=True, unique=True)),
                ('nome', models.CharField(blank=True, max_length=60, null=True)),
                ('faixa_salarial', models.DecimalField(decimal_places=2, max_digits=9)),
                ('requisitos', models.TextField(blank=True, max_length=2000, null=True)),
                ('data_criacao', models.DateTimeField(auto_now=True)),
                ('atualizado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('escolaridade', models.ManyToManyField(to='vagas.EscolaridadeVaga')),
                ('requisitos_adicionais', models.ManyToManyField(to='vagas.RequisitosVaga')),
            ],
        ),
    ]