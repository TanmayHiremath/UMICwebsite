# Generated by Django 3.0.7 on 2020-06-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_month_yr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anouncements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('month_yr', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
