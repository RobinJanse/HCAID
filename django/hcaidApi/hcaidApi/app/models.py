from django.db import models

class BadApply(models.Model):
    age = models.IntegerField()
    gender = models.BooleanField()
    country = models.CharField(max_length=2)
    seek_help = models.BooleanField()
    tech_company = models.BooleanField()
    remote_work = models.BooleanField()

class BadPrediction(models.Model):
    goodEmployee = models.BooleanField()

class GoodApply(models.Model):
    age = models.IntegerField()
    gender = models.BooleanField()
    country = models.CharField(max_length=2)
    seek_help = models.BooleanField()
    tech_company = models.BooleanField()
    remote_work = models.BooleanField()

class GoodPrediction(models.Model):
    goodEmployee = models.BooleanField()