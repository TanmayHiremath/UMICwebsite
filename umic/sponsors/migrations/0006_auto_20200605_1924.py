# Generated by Django 3.0 on 2020-06-05 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0005_auto_20200605_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='sponsor_pic',
            new_name='image',
        ),
    ]
