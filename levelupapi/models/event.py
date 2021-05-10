from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey

class Event(models.Model):
    event_date = models.DateTimeField()
    time = models.TimeField(default="12:00")
    date_created = models.DateTimeField(default=timezone.now)
    game = ForeignKey("Game", on_delete=DO_NOTHING, null=True)
    organizer = ForeignKey("Gamer", on_delete=CASCADE)
    description = models.CharField(max_length=200,default="")
    # Allows model to grab all attendees; no need for loops,
    # And don't need to JOIN therough SQL
    # related_name will be an attribute on Gamer containing all events
    attendees = models.ManyToManyField("Gamer", through=("EventAttendance"), related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
