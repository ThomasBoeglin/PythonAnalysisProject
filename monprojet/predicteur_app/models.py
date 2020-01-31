from django.db import models

# Create your models here.

class Individu(models.Model):
    ChestACCX = models.FloatField()
    ChestACCY = models.FloatField()
    ChestACCZ = models.FloatField()
    ChestECG = models.FloatField()
    ChestResp = models.FloatField()
    WristACCX = models.FloatField()
    WristACCY = models.FloatField()
    WristACCZ = models.FloatField()
    WristBVP = models.FloatField()
    Weight = models.FloatField()
    Gender = models.FloatField()
    Age = models.FloatField()
    Height = models.FloatField()
    Sport = models.FloatField()
    #y to predict
    activity = models.FloatField(null=True)


