# Generated by Django 4.2.10 on 2024-02-11 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('name',), 'verbose_name': 'movie', 'verbose_name_plural': 'movies'},
        ),
    ]
