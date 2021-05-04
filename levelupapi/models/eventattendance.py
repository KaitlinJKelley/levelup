from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db import models
from django.db.models.fields.related import ForeignKey

class EventAttendance(models.Model):
    event = ForeignKey("Event", on_delete=CASCADE)
    gamer = ForeignKey("Gamer", on_delete=CASCADE)