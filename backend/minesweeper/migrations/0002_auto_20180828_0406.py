# Generated by Django 2.1 on 2018-08-28 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(default=0)),
                ('columns', models.IntegerField(default=0)),
                ('num_mines', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='tile',
            old_name='position',
            new_name='column',
        ),
        migrations.RenameField(
            model_name='tile',
            old_name='mines_around',
            new_name='neighbouring_mines',
        ),
        migrations.AddField(
            model_name='tile',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tile',
            name='status',
            field=models.CharField(choices=[('Closed', 'Closed'), ('Opened', 'Opened'), ('Flagged', 'Flagged')], max_length=7),
        ),
        migrations.AddField(
            model_name='game',
            name='difficulty',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='minesweeper.Difficulty'),
        ),
    ]