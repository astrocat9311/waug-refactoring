# Generated by Django 3.2.2 on 2021-05-24 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoption',
            name='product',
        ),
    ]
