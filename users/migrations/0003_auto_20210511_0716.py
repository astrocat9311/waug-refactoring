# Generated by Django 3.1.4 on 2021-05-11 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210511_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 10, 7, 16, 47, 351189)),
        ),
    ]
