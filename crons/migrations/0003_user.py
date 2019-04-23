# Generated by Django 2.2 on 2019-04-23 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crons', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('salt', models.CharField(max_length=16)),
                ('createtime', models.DateTimeField(verbose_name='create time')),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
    ]
