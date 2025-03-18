from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    first_name = models.CharField(
        max_length=200, verbose_name="Имя", help_text="Укажите имя"
    )
    last_name = models.CharField(
        max_length=200, verbose_name="Фамилия", help_text="Укажите фамилию"
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", help_text="Укажите телефон"
    )
    city = models.CharField(
        max_length=150,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        blank=True,
        null=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email}"
