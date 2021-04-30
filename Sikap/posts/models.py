from django.db import models
from datetime import datetime


class Posts(models.Model):
    YoE = models.IntegerField()
    industry = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField()
    dateadded = models.DateField()

    class Meta:
        db_table = "Posts"

