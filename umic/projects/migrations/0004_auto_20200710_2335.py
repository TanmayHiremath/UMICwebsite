# Generated by Django 3.0 on 2020-07-10 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200620_0630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id']},
        ),
    ]
