from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    # photo refers to the brand banner in the catalog list view, not sure if its correct
    # brand_image = models.ImageField(upload_to=None[, height_field=None, width_field=None, max_length=100])

    def __unicode__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Promotion(models.Model):
    brand = models.ForeignKey(Brand)
    promo_name = models.CharField(max_length=100)
    promo_description = models.TextField()
    points_required = models.PositiveIntegerField(max_length=4)

    def __unicode__(self):
        return u'%s %s' % (self.brand, self.promo_name)

class BrandUser(models.Model):
    brand = models.ForeignKey(Brand)
    user = models.ForeignKey(User)
    # will points_earned ever be null? or will this entry only be created when a point is earned?
    points_earned = models.PositiveIntegerField(blank=True, null=True)

# for status choices for BrandUserPromotion
status_choices = (
    ('E', 'Earned'),
    ('U', 'Unearned'),
    ('R', 'Redeemed'),
)

class BrandUserPromotion(models.Model):
    branduser = models.ForeignKey(BrandUser)
    promotion = models.ForeignKey(Promotion)
    status = models.CharField(max_length=1, choices=status_choices)

class Product(models.Model):
    brand = models.ForeignKey(Brand)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    # not sure if product_image is correct to use ImageField plus those options??
    # product_image = models.ImageField(upload_to=None[, height_field=None, width_field=None, max_length=100])
    product_points = models.PositiveIntegerField(max_length=3, default="10")

    def __unicode__(self):
        return u'%s %s' % (self.brand, self.product_name)
