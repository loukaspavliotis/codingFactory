from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .dao import UserDAO, ProfileDAO
from .dto import PlatformStatsDTO
from .serializers import PlatformStatsDTOSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def platform_stats(request):
    """API endpoint to get platform statistics."""
    total_users = UserDAO.get_total_users()
    active_users = UserDAO.get_active_users()
    latest_users = ProfileDAO.get_latest_users()
    active_user_percentage = (active_users / total_users) * 100 if total_users > 0 else 0

    stats_dto = PlatformStatsDTO(
        total_users=total_users,
        active_users=active_users,
        latest_users=latest_users,
        active_user_percentage = active_user_percentage 
    )

    serializer = PlatformStatsDTOSerializer(stats_dto)
    return Response(serializer.data)
