# Generated by Django 2.2 on 2019-04-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crons', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='host_id',
            field=models.IntegerField(default=0),
        ),
    ]
