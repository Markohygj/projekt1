from django.db import models

class Room(models.Model):
    name = models.CharField(max_length= 50)
    type = models.CharField(max_length= 50)
    room_number = models.IntegerField(unique= True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} by {self.type}'

class Workers(models.Model):
    worker_name = models.CharField(max_length= 30)
    worker_id = models.IntegerField(unique= True)

    def __str__(self):
        return f'{self.worker_name} type {self.worker_id}'

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms_booking")
    payment_date = models.DateField()
    date_of_purchase = models.DateField()