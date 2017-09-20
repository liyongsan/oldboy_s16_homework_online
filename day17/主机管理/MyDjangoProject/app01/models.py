from django.db import models

# Create your models here.

class DePart(models.Model):
    title = models.CharField(max_length=16)

class HostList(models.Model):
    hostname = models.CharField(max_length=32)
    port = models.IntegerField()
    dp = models.ForeignKey(to="DePart",to_field="id")

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    uuu = models.ManyToManyField("HostList")

class GroupHost(models.Model):
    title = models.CharField(max_length=32)
    gh = models.ManyToManyField(HostList)
    m = models.ManyToManyField("GroupHost")









