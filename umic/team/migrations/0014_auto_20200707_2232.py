# Generated by Django 3.0 on 2020-07-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0013_auto_20200619_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='dept',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notablealumni',
            name='current_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notablealumni',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='oc',
            name='fb',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='oc',
            name='linkedin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='oc',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='oc',
            name='project',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='oc',
            name='yr_dept',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pastoc',
            name='current_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pastoc',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='fb',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='linkedin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='project',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='subsystem',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='yr_dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='fb',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='linkedin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='project',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='subsystem',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='yr_dept',
            field=models.CharField(max_length=100, null=True),
        ),
    ]