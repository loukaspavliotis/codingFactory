from rest_framework import serializers
from .dto import PlatformStatsDTO, UserSummaryDTO


class UserSummaryDTOSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField()


class PlatformStatsDTOSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    latest_users = UserSummaryDTOSerializer(many=True)