from django.db import models
from datetime import datetime


class Posts(models.Model):
    yearsOfExperience = models.IntegerField()
    industry = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField()
    dateadded = models.DateField()
    email = models.CharField(max_length = 100)
    isAgeViewable = models.IntegerField()

    class Meta:
        db_table = "Posts"

