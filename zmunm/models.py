from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)


class Project(models.Model):
    company = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    memo = models.CharField(max_length=500)
    reg_date = models.DateField(auto_created=True, auto_now=True)
