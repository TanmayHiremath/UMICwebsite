# Generated by Django 3.0 on 2020-06-08 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20200608_1404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentAdvisors',
            new_name='StudentAdvisor',
        ),
        migrations.RenameModel(
            old_name='TeamMembers',
            new_name='TeamMember',
        ),
    ]