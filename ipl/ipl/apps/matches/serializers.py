from rest_framework import serializers

from matches.service.match_service import MatchService


class MatchStatSerializer(serializers.Serializer):
    year = serializers.CharField()
    top_4_team = serializers.SerializerMethodField()
    most_toss_win_team = serializers.SerializerMethodField()
    player_of_match = serializers.SerializerMethodField()
    top_team = serializers.SerializerMethodField()
    most_win_location = serializers.SerializerMethodField()
    toss_winner_decide_bat = serializers.SerializerMethodField()
    top_hosted_location = serializers.SerializerMethodField()
    won_by_highest_run_margin = serializers.SerializerMethodField()
    won_by_highest_wicket_margin = serializers.SerializerMethodField()
    team_win_toss_and_match = serializers.SerializerMethodField()

    def get_top_4_team(self, instance):
        return MatchService().get_top_4_team(instance.year)

    def get_most_toss_win_team(self, instance):
        return MatchService().get_most_toss_win_team(instance.year)

    def get_player_of_match(self, instance):
        return MatchService().get_player_of_match(instance.year)

    def get_top_team(self, instance):
        return MatchService().get_top_team(instance.year)

    def get_most_win_location(self, instance):
        return MatchService().get_most_win_location(instance.year)

    def get_toss_winner_decide_bat(self, instance):
        return MatchService().get_toss_winner_decide_bat(instance.year)

    def get_top_hosted_location(self, instance):
        return MatchService().get_top_hosted_location(instance.year)

    def get_won_by_highest_run_margin(self, instance):
        return MatchService().get_won_by_highest_run_margin(instance.year)

    def get_won_by_highest_wicket_margin(self, instance):
        return MatchService().get_won_by_highest_wicket_margin(instance.year)

    def get_team_win_toss_and_match(self, instance):
        return MatchService().get_team_win_toss_and_match(instance.year)