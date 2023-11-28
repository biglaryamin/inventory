from django.contrib import admin
from .models import Item

from imagekit.admin import AdminThumbnail


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "description",
        "status",
        "delivery_date",
        "image_display",
        "image",
    )

    image_display = AdminThumbnail(image_field="avatar_thumbnail")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]  # this is for the change form
