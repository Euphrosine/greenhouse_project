from django.db import models

class GreenhouseData(models.Model):
    timestamp = models.DateTimeField()
    moisture1 = models.FloatField(null=True)
    moisture2 = models.FloatField(null=True)
    temperature1 = models.FloatField(null=True)
    temperature2 = models.FloatField(null=True)
    humidity1 = models.FloatField(null=True)
    humidity2 = models.FloatField(null=True)

    def __str__(self):
      return f"Greenhouse Data - ID: {self.id}"
