from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Item(models.Model):
    name = models.CharField(max_length=40)
    number = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    avatar_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )

    ITEM_STATUS = (
        ("o", "operational"),
        ("n", "non-operational"),
    )

    status = models.CharField(
        max_length=1,
        choices=ITEM_STATUS,
        default="o",
        help_text="Current status of the item",
    )

    delivery_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "number", "status")
        verbose_name = "کالا"
        verbose_name_plural = "کالاها"
