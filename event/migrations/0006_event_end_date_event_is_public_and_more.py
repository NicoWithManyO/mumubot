# Generated by Django 4.0.6 on 2022-08-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='max_participants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
