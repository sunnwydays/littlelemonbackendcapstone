from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'