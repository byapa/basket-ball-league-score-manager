from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def average_score(self):
        scores = self.scores.all()
        int_scores = [score.score for score in scores]
        if not int_scores:
            return 0.0
        return sum(int_scores)/len(int_scores)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    height_in_cm = models.DecimalField(max_digits=5, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'players')

    @property
    def average_score(self):
        scores = self.scores.all()
        int_scores = [score.score for score in scores]
        if not int_scores:
            return 0.0
        return sum(int_scores)/len(int_scores)

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

@receiver(pre_save, sender=Team)
def check_coach_user_group(sender, instance, **kwargs):
    coach_group = Group.objects.get(name='coach')
    if instance.coach.groups.filter(id=coach_group.id).exists():
        # Coach is in the "coach" group
        pass
    else:
        raise ValueError('Coach must be in the "coach" group.')