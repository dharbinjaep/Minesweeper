# Generated by Django 2.1 on 2018-08-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0008_game_opened_tiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='is_exploded_mine',
            field=models.BooleanField(default=False),
        ),
    ]
