from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)

class Player(models.Model):
    name = models.CharField(max_length=200)
    height_in_cm = models.DecimalField(max_digits=5, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'players')

class Game(models.Model):
    played_on = models.DateTimeField()

class Score(models.Model):
    score = models.IntegerField()

class IndividualScore(Score):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='individual_scores')

class TeamScore(Score):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'scores')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='team_scores')

