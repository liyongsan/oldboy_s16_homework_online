from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=128,unique=True)
    pwd = models.CharField(max_length=128,unique=True)


# ForeignKey
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()


# ManyToManyField
class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'person'))

class Membership(models.Model):
    group = models.ForeignKey(Group)
    person = models.ForeignKey(Person)
    inviter = models.ForeignKey(Person, related_name="membership_invites")
    invite_reason = models.CharField(max_length=64)