from django.db import models

class UserDetails(models.Model):
    userId = models.IntegerField()
    hourlyRate = models.IntegerField()
    phone = models.CharField(max_length=20)
    routingNumber = models.CharField(max_length=30)
    accountNumber = models.CharField(max_length=30)
