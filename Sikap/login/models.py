from django.db import models

class User(models.Model):
    account_type = models.IntegerField()
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    user_type = models.IntegerField()
    isVerified = models.IntegerField()
    companyName = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "User"

class MyUser(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    user_type = models.IntegerField()
    isVerified = models.IntegerField()

    class Meta:
        abstract = True
        ordering = ['email']

class Employer(MyUser):
    companyName = models.CharField(max_length = 100)

    class Meta:
        db_table = "Employer"


class Applicant(MyUser):
    industry = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField()

    class Meta:
        db_table = "Applicant"


# Create your models here.
