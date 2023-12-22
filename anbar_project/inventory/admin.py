from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Item

from imagekit.admin import AdminThumbnail


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

    search_fields = ["name", "status", "description", "delivery_date"]
    image_display = AdminThumbnail(image_field="avatar_thumbnail")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]  # this is for the change form

    @admin.action(description="change to non-operational")
    def make_non_operational(modeladmin, request, queryset):
        queryset.update(status="n")

    actions = ["make_non_operational"]


admin.site.register(Item, ItemAdmin)
