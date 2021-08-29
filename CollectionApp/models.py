from django.db import models

# Create your models here.
class Bin(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()

    class Meta:
        unique_together = (("bin", "operation"),)