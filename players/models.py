from django.db import models

# Create your models here.
class Player(models.Model):
    full_name = models.CharField(max_length=100)
    goals_scored = models.IntegerField()
    birth_date = models.DateField()
