from levelupapi.models.gamer import Gamer
from django.db.models.deletion import DO_NOTHING
from levelupapi.models.event import Event
from django.db import models
from django.db.models.fields.related import ForeignKey

class Event_Attendance(models.Model):
    event = ForeignKey(Event, on_delete=DO_NOTHING)
    gamer = ForeignKey(Gamer, on_delete=DO_NOTHING)