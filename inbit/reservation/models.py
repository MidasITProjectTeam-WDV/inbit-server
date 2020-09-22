from django.db import models

# Create your models here.


class Reservation(models.Model):
    room_id = models.ForeignKey("room.Room",on_delete=models.CASCADE)
    email = models.ForeignKey("user.User",on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    period = models.IntegerField()


class Reservation_queue(models.Model):
    room_id = models.ForeignKey("room.Room",on_delete=models.CASCADE)
    email = models.ForeignKey("user.User",on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    period = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)




    