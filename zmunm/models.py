from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)
