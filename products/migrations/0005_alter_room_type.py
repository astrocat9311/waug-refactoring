# Generated by Django 3.2.2 on 2021-05-13 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_servicetype_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.roomtype'),
        ),
    ]
