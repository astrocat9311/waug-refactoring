# Generated by Django 3.2.2 on 2021-05-26 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_coupon_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 25, 5, 30, 31, 383344)),
        ),
    ]
