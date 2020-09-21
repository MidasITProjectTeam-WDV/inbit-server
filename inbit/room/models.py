from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    max_people = models.IntegerField()
    cur_state = models.BooleanField(default=True)