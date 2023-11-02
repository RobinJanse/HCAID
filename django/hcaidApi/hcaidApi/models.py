from django.db import models

class Survey(models.Model):
    question = models.CharField(max_length=255)

class Prediction(models.Model):
    result = models.CharField(max_length=255)