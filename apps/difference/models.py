from django.db import models

class DifferenceRequest(models.Model):
    number = models.IntegerField(unique=True)
    occurrences = models.PositiveIntegerField(default=0)
    last_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request for n={self.number} - Occurrences: {self.occurrences}"
