from django.db import models

class Policy(models.Model):
    external_user_id = models.CharField(max_length=200)
    benefit = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    total_max_amount = models.IntegerField()

class Payment(models.Model):
    external_user_id = models.CharField(max_length=200)
    benefit = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    amount = models.IntegerField()
    authorized = models.BooleanField()
    reason = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
