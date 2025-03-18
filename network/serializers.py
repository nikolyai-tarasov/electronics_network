from rest_framework import serializers

from .models import Contact, Network, Product


class ContactSerializer(serializers.ModelSerializer):
    """Сериалалазер для модели Контактов"""

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """Сериалалазер для модели Продуктов"""

    class Meta:
        model = Product
        fields = "__all__"


class NetworkSerializer(serializers.ModelSerializer):
    """Сериалалазер для модели Сети"""

    contact = ContactSerializer()
    products = ProductSerializer(many=True)
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Network.objects.all(), allow_null=True
    )
    element = serializers.ReadOnlyField()

    class Meta:
        model = Network
        fields = "__all__"

    def create(self, validated_data):
        contact_data = validated_data.pop("contact")
        product_data = validated_data.pop("products")
        contact = Contact.objects.create(**contact_data)
        network = Network.objects.create(contact=contact, **validated_data)

        product_objects = []
        for product_data_item in product_data:
            product, created = Product.objects.get_or_create(**product_data_item)
            product_objects.append(product)

        network.products.set(product_objects)
        return network

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact", None)
        products_data = validated_data.pop("products", None)

        instance.unit_name = validated_data.get("unit_name", instance.unit_name)
        instance.supplier = validated_data.get("supplier", instance.supplier)

        if contact_data:
            contact_serializer = ContactSerializer(instance.contact, data=contact_data)
            contact_serializer.is_valid(raise_exception=True)
            contact_serializer.save()

        if products_data:

            product_objects = []
            for product_data_item in products_data:
                product, created = Product.objects.get_or_create(**product_data_item)
                product_objects.append(product)
            instance.products.set(product_objects)

        instance.save()
        return instance
