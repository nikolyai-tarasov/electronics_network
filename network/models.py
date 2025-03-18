from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """Модель контактов"""

    email = models.EmailField(unique=True)
    country = models.CharField(
        max_length=50, verbose_name="country", help_text="Название страны"
    )
    city = models.CharField(
        max_length=50, verbose_name="city", help_text="Название города"
    )
    street = models.CharField(
        max_length=50, verbose_name="street", help_text="Название улица"
    )
    house_number = models.IntegerField(help_text="Номер дома")

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house_number}"


class Product(models.Model):
    """Модель продуктов"""

    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.model}"


class Network(models.Model):
    """Модель сети"""

    ELEMENT_CHOICES = [
        ("завод", "Завод"),
        ("индивидуальный предприниматель", "Индивидуальный Предприниматель"),
        ("розничная сеть", "Розничная Сеть"),
    ]
    unit_name = models.CharField(
        max_length=120, verbose_name="name", help_text="Название звена"
    )
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="supplier_link",
    )
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    creation_time = models.DateTimeField(default=timezone.now)
    element = models.CharField(choices=ELEMENT_CHOICES)

    def __str__(self):
        return self.unit_name
