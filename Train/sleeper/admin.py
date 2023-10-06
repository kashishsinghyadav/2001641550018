from django.contrib import admin
from sleeper.models import Trainspecificdata

class Sleep(admin.ModelAdmin):
    list_display=('trainName','trainNumber','departureTimeHours','departureTimeMinutes','departureTimeSeconds','seatsAvailableSleeper','seatsAvailableAC','priceSleeper','priceAC','delayedBy')

admin.site.register(Trainspecificdata,Sleep)
# Register your models here.
