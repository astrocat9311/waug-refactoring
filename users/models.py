from django.db import models

class User(models.Model):
    email        = models.EmailField(max_length=100)
    password     = models.CharField(max_length=500)
    name         = models.CharField(max_length=45)
    last_name    = models.CharField(max_length=45, null=True)
    first_name   = models.CharField(max_length=45, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    image_url    = models.URLField(max_length=2000, null=True)
    coupon       = models.ManyToManyField('Coupon', through='UserCoupon')

    class Meta:
        db_table = 'users'

class Coupon(models.Model):
    name          = models.CharField(max_length=45)
    code          = models.CharField(max_length=45)
    discount_rate = models.DecimalField(max_digits=2, decimal_places=0)
    created_at    = models.DateTimeField(auto_now_add=True)
    expire_date   = models.DateField()

    class Meta:
        db_table = 'coupons'

class UserCoupon(models.Model):
    user   = models.ForeignKey('User', on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_coupons'

class Wishlist(models.Model):
    user    = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlists'
    