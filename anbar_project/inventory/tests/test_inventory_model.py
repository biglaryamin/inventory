from django.test import TestCase
from ..models import Item

class TestItemModel(TestCase):

    def test_create_item(self):
        item = Item.objects.create(
            name = "test",
            number = 2,
            description = "Something Something Something",
            status = "o"
        )
        self.assertEquals(item.name, "test")
        self.assertEquals(item.number, 2)
        self.assertEquals(item.description, "Something Something Something")
        self.assertEquals(item.status, "o")


