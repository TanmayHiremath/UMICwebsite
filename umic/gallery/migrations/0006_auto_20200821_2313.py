# Generated by Django 3.0 on 2020-08-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_merge_20200723_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='serial_number',
            field=models.FloatField(default=1),
        ),
    ]
