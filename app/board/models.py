from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Posts(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Categories)
    user = models.ForeignKey(Users, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    content = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, null=True)
    user = models.ForeignKey(Users, null=True)

    def __str__(self):
        return self.content

