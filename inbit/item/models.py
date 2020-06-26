from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
