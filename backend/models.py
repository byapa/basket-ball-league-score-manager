from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)

class Player(models.Model):
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'players')

class Game(models.Model):
    played_on = models.DateTimeField()

class IndividualScore(models.Model):
    score = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='individual_scores')

class TeamScore(models.Model):
    score = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'scores')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='team_scores')

