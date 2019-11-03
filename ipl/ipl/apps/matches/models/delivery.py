from core.models import AbstractBaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.validators import validate_ball_in_over


class Delivery(AbstractBaseModel):
    match = models.ForeignKey(
        'matches.Match',
        verbose_name=_('match id'),
        on_delete=models.CASCADE
    )
    inning = models.IntegerField(
        _('inning')
    )
    batting_team = models.CharField(
        _('batting team'),
        max_length=50
    )
    bowling_team = models.CharField(
        _('bowling team'),
        max_length=50
    )
    over = models.IntegerField(
        _('over'),
    )
    ball = models.IntegerField(
        _('ball'),
        validators=[validate_ball_in_over]
    )
    batsman = models.CharField(
        _('batsman'),
        max_length=50
    )
    non_striker = models.CharField(
        _('non striker'),
        max_length=50
    )
    bowler = models.CharField(
        _('bowler'),
        max_length=50
    )
    is_super_over = models.BooleanField(
        _('is super over'),
        default=False
    )
    wide_runs = models.IntegerField(
        _('wide run')
    )
    bye_runs = models.IntegerField(
        _('bye runs')
    )
    legbye_runs = models.IntegerField(
        _('legbye runs')
    )
    noball_runs = models.IntegerField(
        _('noball_runs')
    )
    penalty_runs = models.IntegerField(
        _('penalty runs')
    )
    batsman_runs = models.IntegerField(
        _('batsman runs')
    )
    extra_runs = models.IntegerField(
        _('extra runs')
    )
    total_runs = models.IntegerField(
        _('total runs')
    )
    player_dismissed = models.CharField(
        _('player dismissed'),
        max_length=50
    )
    dismissal_kind = models.CharField(
        _('dismissed kind'),
        max_length=25
    )
    fielder = models.CharField(
        _('fielder'),
        max_length=50
    )

    class Meta:
        db_table = 'delivery'

    def __str__(self):
        return f'{self.batting_team} -> {self.bowling_team} | {self.total_run}'
