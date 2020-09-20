# Generated by Django 3.0 on 2020-06-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('sponsor_pic', models.ImageField(default='sponsors/img/favicon.png', upload_to='sponsors/static/img/')),
            ],
        ),
    ]