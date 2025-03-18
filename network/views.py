from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from network.models import Contact, Network, Product
from network.permissions import IsActiveEmployee
from network.serializers import ContactSerializer, NetworkSerializer, ProductSerializer


class CreateNetwork(generics.CreateAPIView):
    """Эндпоинт создания элемента сети"""

    serializer_class = NetworkSerializer
    permission_classes = [IsActiveEmployee]


class RetrieveNetwork(generics.RetrieveAPIView):
    """Эндпоинт просмотра элемента сети"""

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActiveEmployee]


class UpdateNetwork(generics.UpdateAPIView):
    """Эндпоинт обновления элемента сети"""

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActiveEmployee]


class DestroyNetwork(generics.DestroyAPIView):
    """Эндпоинт удаления элемента сети"""

    queryset = Network.objects.all()
    permission_classes = [IsActiveEmployee]


class ListNetwork(generics.ListAPIView):
    """Эндпоинт списка элементов сети"""

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_filters = ["unit_name", "contact__city"]
    ordering_fields = ["unit_name", "debt"]
    filterset_fields = ("contact__country",)
    permission_classes = [IsActiveEmployee]


class CreateProduct(generics.CreateAPIView):
    """Эндпоинт создания продукта элемента сети"""

    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class RetrieveProduct(generics.RetrieveAPIView):
    """Эндпоинт просмотра продукта сети"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveEmployee]


class UpdateProduct(generics.UpdateAPIView):
    """Эндпоинт обновления продукта сети"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveEmployee]


class DestroyProduct(generics.DestroyAPIView):
    """Эндпоинт удаления продукта сети"""

    queryset = Product.objects.all()
    permission_classes = [IsActiveEmployee]


class ListProduct(generics.ListAPIView):
    """Эндпоинт списка продуктов сети"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class CreateContact(generics.CreateAPIView):
    """Эндпоинт создания контактов сети"""

    serializer_class = ContactSerializer
    permission_classes = [IsActiveEmployee]


class RetrieveContact(generics.RetrieveAPIView):
    """Эндпоинт просмотр контактов сети"""

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsActiveEmployee]


class UpdateContact(generics.UpdateAPIView):
    """Эндпоинт обновления контактов сети"""

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsActiveEmployee]


class DestroyContact(generics.DestroyAPIView):
    """Эндпоинт удаления контактов сети"""

    queryset = Contact.objects.all()
    permission_classes = [IsActiveEmployee]


class ListContact(generics.ListAPIView):
    """Эндпоинт список контактов сети"""

    queryset = Contact.objects.all()
    permission_classes = [IsActiveEmployee]
    serializer_class = ContactSerializer
