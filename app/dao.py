from django.contrib.auth.models import User
from django.db.models import Count
from .dto import UserSummaryDTO

class UserDAO:
    @staticmethod
    def create_user(user_dto):
        """Create a new user using UserCreateDTO."""
        user = User.objects.create_user(
            username=user_dto.username,
            password=user_dto.password,
            email=user_dto.email
        )
        return user

    @staticmethod
    def get_user_by_id(user_id):
        """Retrieve a user by their ID."""
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_all_users():
        """Retrieve all users."""
        return User.objects.all()

    @staticmethod
    def delete_user(user):
        """Delete a user."""
        user.delete()

    @staticmethod
    def update_user(user, user_data):
        """Update a user with the given data."""
        user.username = user_data['username']
        user.email = user_data['email']
        # Include other fields as needed
        user.save()

    @staticmethod
    def get_total_users():
        """Get the total number of users."""
        return User.objects.count()

    @staticmethod
    def get_active_users():
        """Get the number of active users."""
        return User.objects.filter(is_active=True).count()


class ProfileDAO:
    @staticmethod
    def get_latest_users(limit=5):
        """Get the latest registered users as UserSummaryDTO."""
        users = User.objects.order_by('-date_joined')[:limit]
        return [
            UserSummaryDTO(
                username=user.username,
                email=user.email,
                date_joined=user.date_joined
            )
            for user in users
        ]

    @staticmethod
    def get_user_email(username):
        """Get user email by username."""
        try:
            user = User.objects.get(username=username)
            return user.email
        except User.DoesNotExist:
            return None