from django.urls import path

from network.apps import NetworkConfig
from network.views import (
    CreateContact,
    CreateNetwork,
    CreateProduct,
    DestroyContact,
    DestroyNetwork,
    DestroyProduct,
    ListContact,
    ListNetwork,
    ListProduct,
    RetrieveContact,
    RetrieveNetwork,
    RetrieveProduct,
    UpdateContact,
    UpdateNetwork,
    UpdateProduct,
)

app_name = NetworkConfig.name

urlpatterns = [
    path("", ListNetwork.as_view(), name="list_network"),
    path("create_network/", CreateNetwork.as_view(), name="create_network"),
    path("update_network/<int:pk>/", UpdateNetwork.as_view(), name="update_network"),
    path("destroy_network/<int:pk>/", DestroyNetwork.as_view(), name="destroy_network"),
    path(
        "retrieve_network/<int:pk>/", RetrieveNetwork.as_view(), name="retrieve_network"
    ),
    path("list_product/", ListProduct.as_view(), name="list_product"),
    path("create_product/", CreateProduct.as_view(), name="create_product"),
    path("update_product/<int:pk>/", UpdateProduct.as_view(), name="update_product"),
    path(
        "retrieve_product/<int:pk>/", RetrieveProduct.as_view(), name="retrieve_product"
    ),
    path("destroy_product/<int:pk>/", DestroyProduct.as_view(), name="destroy_product"),
    path("list_contact/", ListContact.as_view(), name="list_contact"),
    path("create_contact/", CreateContact.as_view(), name="create_contact"),
    path("update_contact/<int:pk>/", UpdateContact.as_view(), name="update_contact"),
    path(
        "retrieve_contact/<int:pk>/", RetrieveContact.as_view(), name="retrieve_contact"
    ),
    path("destroy_contact/<int:pk>/", DestroyContact.as_view(), name="destroy_contact"),
]
