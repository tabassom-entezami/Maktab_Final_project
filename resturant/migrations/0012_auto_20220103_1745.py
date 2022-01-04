# Generated by Django 3.2.9 on 2022-01-03 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customer_device'),
        ('resturant', '0011_auto_20220103_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='is_open',
            field=models.BooleanField(choices=[(0, 'Open'), (1, 'Close')], default=False, verbose_name='IsOpen'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customeraddress_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custumer_address', to='accounts.customeradress'),
        ),
    ]