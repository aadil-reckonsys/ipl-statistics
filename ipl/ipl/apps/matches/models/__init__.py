from .delivery import Delivery
from .match import Match


class MatchYear:
    def __init__(self, year):
        self.year = year


__all__ = ('Match', 'Delivery', 'MatchYear')
