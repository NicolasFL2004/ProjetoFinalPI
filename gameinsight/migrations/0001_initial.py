# Generated by Django 5.1.3 on 2024-11-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('desenvolvedora', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('classificacao', models.CharField(max_length=50)),
                ('data_lancamento', models.DateField()),
                ('comentario', models.TextField()),
                ('nota', models.IntegerField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capas/')),
                ('genero', models.ManyToManyField(to='gameinsight.genero')),
                ('plataforma', models.ManyToManyField(to='gameinsight.plataforma')),
            ],
        ),
    ]
