from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=50)
    country = models.CharField(max_length = 100)

class Player(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)








# Create your models here.
