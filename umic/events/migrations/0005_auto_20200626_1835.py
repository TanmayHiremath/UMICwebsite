# Generated by Django 3.0.7 on 2020-06-26 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_anouncements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Anouncements',
            new_name='Announcement',
        ),
    ]
