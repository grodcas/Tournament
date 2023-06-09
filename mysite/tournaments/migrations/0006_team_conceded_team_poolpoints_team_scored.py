# Generated by Django 4.2 on 2023-04-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_rename_score_match_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='conceded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='poolpoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='scored',
            field=models.IntegerField(default=0),
        ),
    ]
