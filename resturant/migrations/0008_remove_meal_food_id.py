# Generated by Django 3.2.9 on 2022-01-01 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0007_remove_order_food_menu_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='food_id',
        ),
    ]