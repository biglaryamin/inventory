# Generated by Django 3.1.13 on 2023-10-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('o', 'operational'), ('n', 'non-operational')], default='o', help_text='Current status of the item', max_length=1)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]