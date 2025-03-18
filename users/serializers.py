from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    """Сериалазер для регистрации пользователей"""

    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "last_name",
            "first_name",
            "phone",
            "city",
            "avatar",
            "password",
            "password2",
        )

    def validate(self, data):
        """Проверка, что пароли совпадают"""

        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data):
        """Создание нового пользователя"""
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатор пользователя"""

    class Meta:
        model = User
        fields = "__all__"
