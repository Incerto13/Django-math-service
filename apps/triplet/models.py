from django.db import models

class TripletRequest(models.Model):
    a: int = models.IntegerField()
    b: int = models.IntegerField()
    c: int = models.IntegerField()
    occurrences: int = models.IntegerField(default=1)
    last_datetime: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Triplet: {self.a}, {self.b}, {self.c}"
