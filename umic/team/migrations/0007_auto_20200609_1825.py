# Generated by Django 3.0 on 2020-06-09 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20200608_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='oc',
            name='project',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='oc',
            name='subsystem',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='project',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='subsystem',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculty', to='team.CurrentTeam'),
        ),
        migrations.AlterField(
            model_name='notablealumni',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notable_alumni', to='team.PastTeam'),
        ),
        migrations.AlterField(
            model_name='oc',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oc', to='team.CurrentTeam'),
        ),
        migrations.AlterField(
            model_name='pastoc',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='past_oc', to='team.PastTeam'),
        ),
        migrations.AlterField(
            model_name='studentadvisor',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advisor', to='team.CurrentTeam'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to='team.CurrentTeam'),
        ),
    ]