# Generated by Django 3.0 on 2020-06-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20200609_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='oc',
            name='fb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oc',
            name='interests',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='oc',
            name='linkedin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='fb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='interests',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
