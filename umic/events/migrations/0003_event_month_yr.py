# Generated by Django 3.0.7 on 2020-06-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200622_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='month_yr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]