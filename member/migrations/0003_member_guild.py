# Generated by Django 4.0.6 on 2022-08-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_rename_referent_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='guild',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]