from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from matches.serializers import MatchStatSerializer
from matches.models import MatchYear


class MatchStatsAPI(GenericAPIView):
    serializer_class = MatchStatSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        stats_serializer = self.get_serializer(MatchYear(self.kwargs['year']))
        return Response(stats_serializer.data, status=status.HTTP_200_OK)
