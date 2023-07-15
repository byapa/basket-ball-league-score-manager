"""Models"""

from django.contrib.auth.models import Group, User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def average_score(self):
        games = self.games.all()
        scores = [game.score for game in games]
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    height_in_cm = models.DecimalField(max_digits=5, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    @property
    def average_score(self):
        games = self.games.all()
        scores = [game.score for game in games]
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


class Game(models.Model):
    played_on = models.DateTimeField()
    round = models.SmallIntegerField()
    teams = models.ManyToManyField(Team, through="GameTeam")
    players = models.ManyToManyField(Player, through="GamePlayer")


class GameTeam(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="games")
    score = models.IntegerField()


class GamePlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="games")
    score = models.IntegerField()


@receiver(pre_save, sender=Team)
def check_coach_user_group(sender, instance, **kwargs):
    coach_group = Group.objects.get(name="coaches")
    if instance.coach.groups.filter(id=coach_group.id).exists():
        # Coach is in the "coach" group
        pass
    else:
        raise ValueError('Coach must be in the "coach" group.')
