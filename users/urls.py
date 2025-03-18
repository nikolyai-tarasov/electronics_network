from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserDestroyAPIView,
    UserRegisterAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("update_user/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path("destroy_user/<int:pk>/", UserDestroyAPIView.as_view(), name="destroy_user"),
    path(
        "retrieve_user/<int:pk>/", UserRetrieveAPIView.as_view(), name="retrieve_user"
    ),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
