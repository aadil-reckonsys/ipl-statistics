from django.utils import timezone
from django.db.models import Count, Max, F
from django.core.cache import cache
from model_utils import Choices
from matches.models import Match


class MatchService:
    cache_types = Choices(
        ('TOP_4_TEAM', 'top_4_team'),
        ('MOST_TOSS_WIN_TEAM', 'most_toss_win_team'),
        ('PLAYER_OF_MATCH', 'player_of_match'),
        ('TOP_TEAM', 'top_team'),
        ('MOST_WIN_LOCATION', 'most_win_location'),
        ('TOSS_WINNER_DECIDE_BAT', 'toss_winner_decide_bat'),
        ('TOP_HOSTED_LOCATION', 'top_hosted_location'),
        # this question is not clear
        ('TOP_HOSTED_LOCATION_WIN', 'top_hosted_location_win'),
        # this question is not clear
        ('TOP_HOSTED_LOCATION_LOSS', 'top_hosted_location_loss'),
        ('WON_BY_HIGHEST_RUN_MARGIN', 'won_by_highest_run_margin'),
        ('WON_BY_HIGHEST_WICKET_MARGIN', 'won_by_highest_wicket_margin'),
        ('TEAM_WIN_TOSS_AND_MATCH', 'team_win_toss_and_match'),
    )

    def clear_cache(self):
        match_obj = Match.objects.all().order_by('date')[0]
        start_year = match_obj.date.year
        while start_year <= timezone.now().year:
            for _type in self.cache_types:
                print(f'Clearing {_type[1]}-{start_year}')
                cache.set(f'{_type[1]}-{start_year}', None)
            start_year += 1

    def get_top_4_team(self, year):
        key = f'{self.cache_types.TOP_4_TEAM}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('winner') \
                .annotate(winner_count=Count('winner')) \
                .order_by('-winner_count') \
                .values_list('winner', flat=True)[:4]
            cache.set(key, list(data))
        return cache.get(key)

    def get_most_toss_win_team(self, year):
        key = f'{self.cache_types.MOST_TOSS_WIN_TEAM}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('toss_winner') \
                .annotate(winner_count=Count('toss_winner')) \
                .order_by('-winner_count') \
                .values_list('toss_winner', flat=True)[0]
            cache.set(key, str(data))
        return cache.get(key)

    def get_player_of_match(self, year):
        key = f'{self.cache_types.PLAYER_OF_MATCH}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('player_of_match') \
                .annotate(winner_count=Count('player_of_match')) \
                .order_by('-winner_count') \
                .values_list('player_of_match', flat=True)[0]
            cache.set(key, str(data))
        return cache.get(key)

    def get_top_team(self, year):
        key = f'{self.cache_types.TOP_TEAM}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = self.get_top_4_team(year)
            cache.set(key, str(data[0]))
        return cache.get(key)

    def get_most_win_location(self, year):
        key = f'{self.cache_types.MOST_WIN_LOCATION}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('venue') \
                .annotate(winner_count=Count('winner')) \
                .order_by('-winner_count') \
                .values_list('venue', flat=True)[0]
            cache.set(key, str(data))
        return cache.get(key)

    def get_toss_winner_decide_bat(self, year):
        key = f'{self.cache_types.TOSS_WINNER_DECIDE_BAT}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            match_data = Match.objects.filter(date__year=year)
            data = match_data.filter(toss_decision='bat').count() / match_data.count()
            cache.set(key, f'{round(data * 100, 2)}%')
        return cache.get(key)

    def get_top_hosted_location(self, year):
        key = f'{self.cache_types.TOP_HOSTED_LOCATION}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('venue') \
                .annotate(venue_count=Count('venue')) \
                .order_by('-venue_count') \
                .values_list('venue', flat=True)[0]
            cache.set(key, str(data))
        return cache.get(key)

    def get_won_by_highest_run_margin(self, year):
        key = f'{self.cache_types.WON_BY_HIGHEST_RUN_MARGIN}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('winner') \
                .annotate(run_diff=Max('win_by_runs')) \
                .order_by('-run_diff') \
                .values_list('winner', flat=True)[0]
            cache.set(key, str(data))
        return cache.get(key)

    def get_won_by_highest_wicket_margin(self, year):
        key = f'{self.cache_types.WON_BY_HIGHEST_WICKET_MARGIN}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year) \
                .values('winner') \
                .annotate(wicket_diff=Max('win_by_wickets')) \
                .order_by('-wicket_diff') \
                .values_list('winner', flat=True)[0]
            cache.set(key, str(data))
        return cache.get(key)

    def get_team_win_toss_and_match(self, year):
        key = f'{self.cache_types.TEAM_WIN_TOSS_AND_MATCH}-{year}'
        cached_data = cache.get(key)
        if not cached_data:
            data = Match.objects.filter(date__year=year).filter(toss_winner=F('winner')).count()
            cache.set(key, str(data))
        return cache.get(key)
