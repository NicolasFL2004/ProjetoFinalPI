# Generated by Django 5.1.4 on 2025-01-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome_bairro',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome_mae',
        ),
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='avatars/'),
        ),
    ]
