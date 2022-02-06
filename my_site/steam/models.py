from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    data_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username



