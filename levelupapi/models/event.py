from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey

class Event(models.Model):
    event_date = models.DateTimeField
    date_created = models.DateTimeField(auto_now_add=True)
    event_address = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
