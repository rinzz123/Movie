# Generated by Django 4.2.10 on 2024-02-12 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_alter_movie_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Category',
            new_name='category',
        ),
    ]
