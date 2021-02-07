from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Player(models.Model):

    name = models.TextField()
    utr_id = models.IntegerField(primary_key=True)
    email = models.TextField()
    homePhone = models.IntegerField()
    mobilePhone = models.IntegerField()
    city = models.TextField(max_length=30)
    country = models.TextField(max_length=30)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    utr = models.IntegerField(validators=[MaxValueValidator(16), MinValueValidator(1)])

    def __str__(self):
        return self.name

class ProPlayer(Player):
    atpRanking = models.IntegerField()
    totalSalary = models.IntegerField()
    monthsOnTour = models.IntegerField()
    

class HighSchoolPlayer(Player):
    school = models.TextField(max_length=30)
    graduating = models.IntegerField()
    recruitingWebsite = models.URLField(max_length=50)
    ustaRanking = models.IntegerField()
    itfRanking = models.IntegerField()






