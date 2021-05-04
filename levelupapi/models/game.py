from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey

# class GamerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gamer
#         fields = ['id', 'name', 'bio']
        
class Game(models.Model):
    name = models.CharField(max_length=50)
    num_of_players = models.CharField(max_length=20)
    gametype = ForeignKey("GameType", on_delete=DO_NOTHING, null=True)
    gamer = ForeignKey("Gamer", on_delete=CASCADE)