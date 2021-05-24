from django.db import models


class Category(models.Model):
    name        = models.CharField(max_length=45)
    image_url   = models.URLField(max_length=2000)

    class Meta:
        db_table = 'categories'


class Area(models.Model):
    name      = models.CharField(max_length=45)
    image_url = models.URLField(max_length=2000)
    category  = models.ManyToManyField('Category',through='CategoryArea')

    class Meta:
        db_table = 'areas'

class CategoryArea(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    area     = models.ForeignKey('Area',on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_areas'

class City(models.Model):
    name = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'cities'


class District(models.Model):
    name = models.CharField(max_length=45)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'districts'


class RoomType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'room_types'


class Room(models.Model):
    name        = models.CharField(max_length=45)
    rating      = models.DecimalField(max_digits=3, decimal_places=1)
    grade       = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    address     = models.CharField(max_length=100, default=None)
    latitude    = models.DecimalField(max_digits=20, decimal_places=17)
    longitude   = models.DecimalField(max_digits=20, decimal_places=17)
    category    = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    area        = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
    city        = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    district    = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    price       = models.DecimalField(max_digits=18, decimal_places=2)
    is_popular  = models.BooleanField(default=False)
    type        = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'rooms'


class ServiceCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'service_categories'


class Service(models.Model):
    name             = models.CharField(max_length=45)
    room             = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'services'


class RoomImage(models.Model):
    image_url = models.URLField(max_length=2000)
    room      = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'room_images'


class ProductType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'product_types'


class Product(models.Model):
    name         = models.CharField(max_length=45)
    rating       = models.DecimalField(max_digits=3, decimal_places=1)
    description  = models.TextField()
    address      = models.CharField(max_length=100)
    latitude     = models.DecimalField(max_digits=20, decimal_places=17)
    longitude    = models.DecimalField(max_digits=20, decimal_places=17)
    category     = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    area         = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
    city         = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    district     = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    price        = models.DecimalField(max_digits=18, decimal_places=2)
    is_popular   = models.BooleanField(default=False)
    type         = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'


class ProductOption(models.Model):
    option  = models.CharField(max_length=45)
    price   = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        db_table = 'product_options'