from django.db import models
from django.utils import timezone

class TripletRequest(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    occurrences = models.IntegerField(default=1)
    last_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Triplet: {self.a}, {self.b}, {self.c}"
