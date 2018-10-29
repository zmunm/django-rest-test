from django.db import models
from django.core.cache import cache


class Language(models.Model):
    name = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)


class Project(models.Model):
    def save(self, *args, **kwargs):
        cache.delete('Project')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete('Project')
        super().delete(*args, **kwargs)
    company = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    memo = models.CharField(max_length=500)
    reg_date = models.DateField(auto_created=True, auto_now=True)
