from django.db import models


class Room(models.Model):
    description = models.CharField(max_length=180)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return ' '.join(self.description.split()[:2])