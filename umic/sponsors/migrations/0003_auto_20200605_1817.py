# Generated by Django 3.0 on 2020-06-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20200605_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_pic',
            field=models.ImageField(blank=True, null=True, upload_to='sponsors/static/img/'),
        ),
    ]