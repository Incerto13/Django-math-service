from django.db import models

class DifferenceRequest(models.Model):
    number: int = models.IntegerField(unique=True)
    occurrences: int = models.PositiveIntegerField(default=0)
    last_datetime: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request for n={self.number} - Occurrences: {self.occurrences}"
