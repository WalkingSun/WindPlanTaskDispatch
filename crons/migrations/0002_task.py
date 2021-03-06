# Generated by Django 2.2 on 2019-04-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=32)),
                ('times', models.CharField(max_length=32)),
                ('command', models.CharField(max_length=64)),
                ('createtime', models.DateTimeField(verbose_name='create time')),
                ('isdelete', models.IntegerField(default=0)),
                ('create_userid', models.IntegerField(default=None)),
                ('create_username', models.CharField(default='', max_length=16)),
            ],
        ),
    ]
