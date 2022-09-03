# Generated by Django 4.0.6 on 2022-08-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_guild'),
        ('event', '0008_alter_event_end_date_alter_event_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.guild'),
        ),
    ]
