# Generated by Django 3.0 on 2020-07-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200710_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['no_image', '-id']},
        ),
        migrations.AddField(
            model_name='project',
            name='no_image',
            field=models.IntegerField(default=0),
        ),
    ]
