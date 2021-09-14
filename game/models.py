from django.db import models


class Character(models.Model):
    type = models.CharField(max_length=20)
    hp = models.IntegerField(default=100)
    mp = models.IntegerField(default=100)


class Player(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    character = models.ManyToManyField(Character)


class Round(models.Model):
    date = models.DateTimeField('game date')
    round_number = models.IntegerField(default=1)
    p1 = models.ManyToManyField(Player, related_name='round_p1')
    p2 = models.ManyToManyField(Player, related_name='round_p2')
