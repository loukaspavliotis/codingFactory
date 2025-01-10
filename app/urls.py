
from django.urls import path
from . import views
from . import api_views
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import manage_users, edit_user, delete_user
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Description of your API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # API routes
    path('api/platform-stats/', api_views.platform_stats, name='platform-stats'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('manage-users/',  views.manage_users, name='manage_users'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]
handler404 = 'app.views.custom_404'