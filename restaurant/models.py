from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name

class Menu(models.Model):
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.FloatField()
    Inventory = models.IntegerField()

    def __str__(self):
        return self.Name