# Generated by Django 3.0 on 2020-07-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='serial_number',
            field=models.IntegerField(default=1),
        ),
    ]