# Generated by Django 4.2.7 on 2023-12-16 13:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0006_alter_item_description_alter_item_image"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="item",
            unique_together={("name", "number", "status")},
        ),
    ]
