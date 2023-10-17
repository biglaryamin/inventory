from django.contrib import admin
from .models import Item


# admin.site.register(Item)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "number",
                    "description",
                    "picture",
                    "status",
                    "delivery_date")