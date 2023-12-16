from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item


@receiver(post_save, sender=Item)
def item_created(sender, instance, created, **kwargs):
    if created:
        print(f"************* Item {instance.name} created ***************")
