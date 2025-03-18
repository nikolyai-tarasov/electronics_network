from django.contrib import admin

from .models import Contact, Network, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "street", "house_number")
    list_filter = ("city", "country")
    search_fields = ("email", "city", "street")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
    list_filter = ("release_date",)
    search_fields = ("name", "model")


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        "unit_name",
        "contact",
        "supplier",
        "debt",
        "creation_time",
        "element",
    )
    list_filter = ("contact__city", "contact__country")
    search_fields = ("unit_name", "contact__email", "contact__city", "contact__street")
    readonly_fields = ("element",)

    fieldsets = (
        (None, {"fields": ("unit_name", "contact", "products", "supplier", "debt")}),
        (
            "ReadOnly Information",
            {"fields": ("element", "creation_time"), "classes": ("collapse",)},
        ),
    )
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt = 0
            obj.save()

    clear_debt.short_description = "Очистить задолженность"

    def city(self, obj):
        return obj.contact.city

    city.short_description = "City"
    city.admin_order_field = "contact__city"

    def country(self, obj):
        return obj.contact.country

    country.short_description = "Country"
    country.admin_order_field = "contact__country"
