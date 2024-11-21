# Generated by Django 5.0.4 on 2024-11-21 05:19

from django.db import migrations
from datetime import date

def add_initial_players(apps, schema_editor):
    Player = apps.get_model('players', 'Player')
    Player.objects.create(full_name='Lionel Messi', goals_scored=850, birth_date=date(1987, 6, 24))
    Player.objects.create(full_name='Manuel Neuer', goals_scored=0, birth_date=date(1986, 3, 27))
    Player.objects.create(full_name='Ronaldinho', goals_scored=266, birth_date=date(1980, 3, 21))

class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_players),
    ]