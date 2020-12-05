from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class MatchOutcome(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'match outcome class'
        verbose_name_plural = 'match outcome classes'

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateTimeField(auto_created=True)
    outcome = models.ForeignKey('match.MatchOutcome', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('match:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'matches'

    def __str__(self):
        return f'{self.date} => {self.outcome}'


class Player(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class MatchPlayer(models.Model):
    match = models.ForeignKey('match.Match', on_delete=models.CASCADE)
    player = models.ForeignKey('match.Player', on_delete=models.CASCADE)

    def __str__(self):
        return self.player.name
