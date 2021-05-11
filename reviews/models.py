from django.db import models

class Review(models.Model):
    dinning     = models.ForeignKey('products.Dinning', on_delete=models.CASCADE)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment     = models.TextField()
    star_review = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'reviews'

class ReviewPhoto(models.Model):
    image_url = models.URLField(max_length=2000)
    review    = models.ForeignKey('Review',on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_photos'
