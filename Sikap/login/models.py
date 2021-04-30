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

    class Meta:
        db_table = "User"
    

# Create your models here.