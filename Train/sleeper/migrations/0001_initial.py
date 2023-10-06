# Generated by Django 4.2.2 on 2023-10-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainspecificdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainName', models.CharField(max_length=100)),
                ('trainNumber', models.CharField(max_length=10)),
                ('departureTimeHours', models.IntegerField()),
                ('departureTimeMinutes', models.IntegerField()),
                ('departureTimeSeconds', models.IntegerField()),
                ('seatsAvailableSleeper', models.IntegerField()),
                ('seatsAvailableAC', models.IntegerField()),
                ('priceSleeper', models.DecimalField(decimal_places=2, max_digits=10)),
                ('priceAC', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delayedBy', models.IntegerField()),
            ],
        ),
    ]