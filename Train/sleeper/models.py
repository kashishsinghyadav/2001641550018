from django.db import models

# Create your models here.
from django.db import models

class Trainspecificdata(models.Model):
    trainName = models.CharField(max_length=100)
    trainNumber = models.CharField(max_length=10)
    departureTimeHours = models.IntegerField()
    departureTimeMinutes = models.IntegerField()
    departureTimeSeconds = models.IntegerField()
    seatsAvailableSleeper = models.IntegerField()
    seatsAvailableAC = models.IntegerField()
    priceSleeper = models.DecimalField(max_digits=10, decimal_places=2)
    priceAC = models.DecimalField(max_digits=10, decimal_places=2)
    delayedBy = models.IntegerField()
