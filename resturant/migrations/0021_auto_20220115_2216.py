# Generated by Django 3.2.9 on 2022-01-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0020_auto_20220115_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='is_open',
            field=models.BooleanField(choices=[(1, 'Close'), (0, 'Open')], default=True, verbose_name='IsOpen'),
        ),
        migrations.AlterField(
            model_name='order',
            name='foodmenu_id',
            field=models.ManyToManyField(related_name='food', through='resturant.OrderItem', to='resturant.FoodMenu'),
        ),
    ]
