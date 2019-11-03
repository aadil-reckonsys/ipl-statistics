from django.core.validators import ValidationError
from django.utils import timezone


def validate_year(value):
    if not (2000 < value <= timezone.now().year):
        raise ValidationError(
            'Unknown year found.'
        )


def validate_ball_in_over(value):
    if not (0 < value <= 6):
        raise ValidationError(
            'Invalid ball entered'
        )
