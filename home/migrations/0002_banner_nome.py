# Generated by Django 3.0 on 2020-08-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='nome',
            field=models.CharField(default='lucas', max_length=100),
        ),
    ]
