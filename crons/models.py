from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# 任务表
class Task(models.Model):
    comment = models.CharField(max_length=32,default='')
    times = models.CharField(max_length=32)
    command = models.CharField(max_length=64)
    createtime = models.DateTimeField('create time')
    isdelete = models.IntegerField(default=0)
    create_userid = models.IntegerField(default=None)
    create_username = models.CharField(max_length=16,default='')
    host_id = models.IntegerField(default=0)

# 用户表
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=16)
    createtime = models.DateTimeField('create time')
    isdelete = models.IntegerField(default=0)

# 机器
class Host(models.Model):
    hostname = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    createtime = models.DateTimeField('create time')
    isdelete = models.IntegerField(default=0)

# 用户机器关联表
class UserHostRelation(models.Model):
    user_id = models.IntegerField()
    host_id = models.IntegerField()
    createtime = models.DateTimeField('create time')
