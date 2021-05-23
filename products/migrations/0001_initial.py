# Generated by Django 3.2.2 on 2021-05-18 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city')),
            ],
            options={
                'db_table': 'districts',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('is_popular', models.BooleanField(default=False)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.area')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.district')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'product_types',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('grade', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.TextField()),
                ('address', models.CharField(default=None, max_length=100)),
                ('latitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('is_popular', models.BooleanField(default=False)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.area')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.district')),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'service_categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.room')),
                ('service_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.servicecategory')),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.room')),
            ],
            options={
                'db_table': 'room_images',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.roomtype'),
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'product_options',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'product_images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.producttype'),
        ),
        migrations.CreateModel(
            name='CategoryArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.area')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'category_areas',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='category',
            field=models.ManyToManyField(through='products.CategoryArea', to='products.Category'),
        ),
    ]
