# Generated by Django 3.0 on 2020-06-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_auto_20200609_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='email',
        ),
        migrations.RemoveField(
            model_name='notablealumni',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pastoc',
            name='email',
        ),
        migrations.AddField(
            model_name='faculty',
            name='dept',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='notablealumni',
            name='current_company',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pastoc',
            name='current_company',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]