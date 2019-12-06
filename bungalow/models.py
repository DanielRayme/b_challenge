from django.db import models

# A model for property listings.  

class PropertyModel(models.Model):
    area_unit = models.CharField(max_length=50)
    bathrooms = models.FloatField(null=True, blank=True)
    bedrooms = models.FloatField(null=True, blank=True)
    home_size = models.FloatField(null=True, blank=True)
    home_type = models.CharField(max_length=20)
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.FloatField(null=True, blank=True)
    link = models.TextField()
    price = models.CharField(max_length=20)
    property_size = models.FloatField(null=True, blank=True)
    rent_price = models.FloatField(null=True, blank=True)
    rentzestimate_amount = models.FloatField(null=True, blank=True)
    rentzestimate_last_updated = models.DateField(null=True, blank=True)
    tax_value = models.FloatField(null=True, blank=True)
    tax_year = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    zestimate_amount = models.FloatField(null=True, blank=True)
    zestimate_last_updated = models.CharField(max_length=15, null=True)
    zillow_id = models.BigIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
 
