from django.db    import models

class Category(models.Model):
    name        = models.CharField(max_length=45)
    image_url   = models.URLField(max_length=2000)
    destination = models.ManyToManyField('Destination', through='CategoryDestination')

    class Meta:
        db_table = 'categories'

class Destination(models.Model):
    name      = models.CharField(max_length=45)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'destinations'

class CategoryDestination(models.Model):
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_destinations'

class City(models.Model):
    name = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'cities'

class District(models.Model):
    name     = models.CharField(max_length=45)
    city     = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'districts'

class RoomType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'room_types'

class Room(models.Model):
    grade   = models.SmallIntegerField(default=0)
    type    = models.ForeignKey('RoomType', on_delete=models.SET_NULL,null=True)
    service = models.ManyToManyField('Service', through='RoomService')

    class Meta:
        db_table = 'rooms'

class ServiceType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'service_types'

class Service(models.Model):
    name         = models.CharField(max_length=45)
    service_type = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'services'

class RoomService(models.Model):
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    service      = models.ForeignKey('Service', on_delete=models.CASCADE)
    room         = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_services'

class DinningType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'dinning_types'

class DinningOption(models.Model):
    option = models.CharField(max_length=45)

    class Meta:
        db_table = 'dinning_options'

class ActivityType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'activity_types'

class Room(models.Model):

    name           = models.CharField(max_length=45)
    rating         = models.DecimalField(max_digits=3,decimal_places=1)
    grade          = models.DecimalField(max_digits=3,decimal_places=1)
    description    = models.TextField()
    address        = models.CharField(max_length=100)
    latitude       = models.DecimalField(max_digits=20, decimal_places=17)
    longitude      = models.DecimalField(max_digits=20, decimal_places=17)
    category       = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    destination    = models.ForeignKey('Destination', on_delete=models.SET_NULL,null=True)
    city           = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
    district       = models.ForeignKey('District', on_delete=models.SET_NULL,null=True)
    price          = models.DecimalField(max_digits=18, decimal_places=2)

class RoomImage(models.Model):
    image_url = models.URLField(max_length=2000)
    product = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'room_images'



    is_dinning     = models.BooleanField(default=False,null=True)
    dinning_type   = models.ForeignKey('DinningType',on_delete=models.SET_NULL,null=True)
    dinning_option = models.ForeignKey('DinningOption',on_delete=models.SET_NULL,null=True)
    is_activity    = models.BooleanField(default=False,null=True)
    activity_type  = models.ForeignKey('ActivityType',on_delete=models.SET_NULL,null=True)
    is_popular     = models.BooleanField(default=False)
    product_type   = models.Choices

    class Meta:
        db_table = 'products'



