from django.db import models

class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.TextField()
    rating  = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        db_table = 'reviews'

class ReviewPhoto(models.Model):
    image_url = models.URLField(max_length=2000)
    review    = models.ForeignKey('Review',on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_photos'
