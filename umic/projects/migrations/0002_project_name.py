# Generated by Django 3.0.7 on 2020-06-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
