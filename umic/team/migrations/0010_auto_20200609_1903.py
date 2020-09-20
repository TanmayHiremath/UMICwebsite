# Generated by Django 3.0 on 2020-06-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_auto_20200609_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oc',
            old_name='dept',
            new_name='yr_dept',
        ),
        migrations.RemoveField(
            model_name='oc',
            name='year',
        ),
        migrations.RemoveField(
            model_name='studentadvisor',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='studentadvisor',
            name='year',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='year',
        ),
        migrations.AddField(
            model_name='studentadvisor',
            name='yr_dept',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='yr_dept',
            field=models.CharField(max_length=20, null=True),
        ),
    ]