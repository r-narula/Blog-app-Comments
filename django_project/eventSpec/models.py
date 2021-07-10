from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=255, default="Event none")
    
    def __str__(self):
        return self.event_name
class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name