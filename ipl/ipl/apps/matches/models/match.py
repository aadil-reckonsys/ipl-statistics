from core.models import AbstractBaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.validators import validate_year


class Match(AbstractBaseModel):
    id = models.IntegerField(
        _('match id'),
    )
    season = models.IntegerField(
        _('season'),
        validators=[validate_year]
    )
    city = models.CharField(
        _('city'),
        max_length=60
    )
    date = models.DateField(
        _('match date')
    )
    team1 = models.CharField(
        _('team 1'),
        max_length=50
    )
    team2 = models.CharField(
        _('team 2'),
        max_length=50
    )
    toss_winner = models.CharField(
        _('toss_winner'),
        max_length=50
    )
    toss_decision = models.CharField(
        _('toss_decision'),
        max_length=10
    )
    result = models.CharField(
        _('result'),
        max_length=10
    )
    dl_applied = models.IntegerField(
        _('dl_applied')
    )
    winner = models.CharField(
        _('winner'),
        max_length=50
    )
    win_by_runs = models.IntegerField(
        _('wins by run')
    )
    win_by_wickets = models.IntegerField(
        _('wins by wicket')
    )
    player_of_match = models.CharField(
        _('player of match'),
        max_length=50
    )
    venue = models.CharField(
        _('venue'),
        max_length=100
    )
    umpire1 = models.CharField(
        _('umpire 1'),
        max_length=50
    )
    umpire2 = models.CharField(
        _('umpire 1'),
        max_length=50
    )
    umpire3 = models.CharField(
        _('umpire 1'),
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'match'

    def __str__(self):
        return f'{self.season} | {self.team1} | {self.team2}'
