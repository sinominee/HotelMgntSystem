from django.db import models

# Create your models here.
class Menu(models.Model):
    Name = models.CharField(max_length=255)
    description = models.TextField()

class Food(models.Model):
    name = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu,on_delete=models.SET_NULL,null=True)

