# Generated by Django 3.0 on 2020-06-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_auto_20200609_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='oc',
            name='dept',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='oc',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='dept',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='fb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='interests',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='linkedin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='project',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='subsystem',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='dept',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
