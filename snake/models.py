from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Player(AbstractUser):

    def __unicode__(self):
        return self.username


# class Game(models.Model):
#     name = models.CharField(max_length=30)
#     best_score = models.IntegerField(null=True)


class Score(models.Model):
    value = models.ForeignKey(Player, related_name='score')
    GAMES = (('SNAKE', 'SNAKE'), ('MEMORY GAME', 'MEMORY GAME'))
    game = models.CharField(max_length=20, choices=GAMES)
    created = models.DateTimeField(auto_now_add=True)