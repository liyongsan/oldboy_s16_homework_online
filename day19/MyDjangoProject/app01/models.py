from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True)

class News_Type_Choices(models.Model):
    content = models.CharField(max_length=32)

class News(models.Model):
    title = models.CharField(max_length=64)
    img = models.CharField(max_length=128)
    summary = models.CharField(max_length=128)
    nt_id = models.ForeignKey("News_Type_Choices")
    u = models.ForeignKey("UserInfo")
    ctime = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.CharField(max_length=256)
    user = models.ForeignKey("UserInfo",related_name="q1")
    new = models.ForeignKey("News",related_name="q2")
    ctime = models.DateTimeField(auto_now_add=True)




