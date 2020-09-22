from django.db import models


# Create your models here.
class Users(models.Model):
    email = models.EmailField("Email",max_length=50, primary_key=True)
    name = models.CharField("Name", max_length=50)
    password = models.CharField("password", max_length=100)
    phone_num = models.IntegerField("phone number")
    position = models.IntegerField("School positino")

    class Meta:
        verbose_name = 'User'
        ordering = ["position"]
    

    def __str__(self):
        return self.email 
    
    