# Generated by Django 4.2.5 on 2023-09-05 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerregistration',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 9, 5, 14, 45, 14, 809892, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sellerregistration',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]