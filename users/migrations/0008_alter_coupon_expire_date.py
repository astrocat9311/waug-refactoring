# Generated by Django 3.2.2 on 2021-05-24 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_coupon_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 23, 5, 36, 56, 781168)),
        ),
    ]
