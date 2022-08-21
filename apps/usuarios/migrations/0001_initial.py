# Generated by Django 3.2.15 on 2022-08-21 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import usuarios.models.models_user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolaridade', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateField(auto_created=True, auto_now=True, db_column='data_cadastro', null=True)),
                ('user_tipo', models.CharField(blank=True, choices=[('U', 'Usuario'), ('E', 'Empresa')], db_column='user_tipo', default='U', max_length=20, null=True)),
                ('escolaridade_user', models.CharField(blank=True, db_column='escolaridade_user', max_length=11, null=True)),
                ('idade', models.IntegerField(blank=True, db_column='idade', default=0, null=True)),
                ('cidade', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], db_column='cidade', max_length=20, null=True)),
                ('contato', models.CharField(blank=True, db_column='contato', max_length=11, null=True)),
                ('endereco', models.CharField(blank=True, db_column='endereco', max_length=20, null=True)),
                ('numero_casa', models.IntegerField(blank=True, db_column='numero_casa', null=True)),
                ('cpf', models.CharField(blank=True, db_column='cpf', max_length=14, null=True)),
                ('cnpj', models.CharField(blank=True, db_column='cnpj', max_length=18, null=True)),
                ('sobre', models.TextField(blank=True, db_column='sobre', max_length=500, null=True)),
                ('github_user', models.CharField(blank=True, db_column='github_user', max_length=100, null=True)),
                ('linkedin_user', models.CharField(blank=True, db_column='linkedin_user', max_length=100, null=True)),
                ('instagram_user', models.CharField(blank=True, db_column='instagram_user', max_length=100, null=True)),
                ('imagem_perfil', models.ImageField(blank=True, db_column='imagem_perfil', default='usuario.png', null=True, upload_to=usuarios.models.models_user.upload_to)),
                ('data_update', models.DateTimeField(auto_now=True, db_column='data_update')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ProfileUser',
                'verbose_name_plural': 'ProfileUsers',
                'db_table': 'profile_user',
            },
        ),
    ]
