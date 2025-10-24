from django.db import models


class Booking(models.Model):
    id_room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.date_start.strftime('%d %B')} - {
            self.date_end.strftime('%d %B')
        }"
