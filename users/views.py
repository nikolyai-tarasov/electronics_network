from rest_framework import generics

from users.models import User
from users.permissions import IsUserOwner
from users.serializers import RegisterUserSerializer, UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    """Эндпоинт создания пользователя"""

    serializer_class = RegisterUserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт вывода страницы пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUserOwner]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUserOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsUserOwner]
