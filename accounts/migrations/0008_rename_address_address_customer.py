# Generated by Django 3.2.9 on 2022-01-06 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220106_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='customer',
        ),
    ]