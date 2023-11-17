from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Item(models.Model):
    name = models.CharField(max_length=40)
    number = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()

    avatar_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})


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


    # def image_tag(self):
    #     from django.utils.html import escape
    #     return u'<img src="%s" />' % escape(<URL to the image>)
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True


    def __str__(self):
        return self.name
