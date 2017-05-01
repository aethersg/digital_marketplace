from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='slug-field')  # unique=True
    description = models.TextField(default='Default value')
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=0.99, null=True, blank=True)

    def __unicode__(self):
        return self.title
