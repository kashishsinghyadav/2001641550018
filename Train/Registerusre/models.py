from django.db import models

class RegisterUser(models.Model):
    companyname=models.CharField(max_length=12)
    ownername=models.CharField(max_length=20)
    rollno=models.CharField(max_length=5)
    owneremail=models.EmailField(max_length=15)
    accesscode=models.CharField(max_length=7)
    


# Create your models here.
