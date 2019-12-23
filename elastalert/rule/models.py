from django.db import models
from datetime import datetime

# Create your models here.
class Rule(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    description = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=200)
    index = models.CharField(max_length=200)
    num_events = models.IntegerField()
    filter = models.TextField(max_length = 1000)
    alert = models.CharField(max_length = 100)
    command = models.CharField(max_length = 400)
    runstatus = models.CharField(max_length=100,default='stopped')

    def __str__(self):
        return(self.name)

