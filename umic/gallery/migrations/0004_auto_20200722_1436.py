# Generated by Django 3.0 on 2020-07-22 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_serial_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['serial_number']},
        ),
    ]
