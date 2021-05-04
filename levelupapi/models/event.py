from django.db import models
import datetime
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey

class Event(models.Model):
    event_date = models.DateTimeField()
    date_created = models.DateTimeField()
    event_address = models.CharField(max_length=100)
    game = ForeignKey("Game", on_delete=DO_NOTHING, null=True)
    gamer = ForeignKey("Gamer", on_delete=CASCADE)
    # Allows model to grab all attendees; no need for loops,
    # And don't need to JOIN therough SQL
    # related_name will be an attribute on Gamer containing all events
    attendees = models.ManyToManyField("Gamer", through=("EventAttendance"), related_name="attending")
