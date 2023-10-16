from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=40)
    number = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField()
    ITEM_STATUS = (
        ('o', 'operational'),
        ('n', 'non-operational'),
    )

    status = models.CharField(
        max_length=1,
        choices=ITEM_STATUS,
        default='o',
        help_text='Current status of the item',
    )

    delivery_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
