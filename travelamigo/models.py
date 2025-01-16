from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bus(models.Model):
    number = models.CharField(max_length=10)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    capacity = models.IntegerField()

    def __str__(self):
        return self.number

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f"{self.bus.number} - {self.date}"
