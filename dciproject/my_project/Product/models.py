from django.db import models



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    product_image_url = models.URLField(max_length=200, blank=True)
    product_price = models.IntegerField()


# Create your models here.
