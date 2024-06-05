from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class RealEstate(models.Model):
    date = models.DateTimeField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    sqft_living = models.IntegerField()
    sqft_lot = models.IntegerField()
    floors = models.FloatField()
    waterfront = models.BooleanField()
    view = models.IntegerField()
    condition = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    yr_built = models.IntegerField()
    yr_renovated = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    statezip = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    predict_price = models.FloatField()
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.statezip}, {self.country}"
    
    def calculate_derived_value(self):
        self.calculated_value = (((self.bedrooms * self.bathrooms*(self.sqft_living / self.sqft_lot) * self.floors) + self.waterfront - self.view)* self.condition*(self.sqft_above + self.sqft_basement)) *100

    def save(self, *args, **kwargs):
        self.calculate_derived_value()
        super().save(*args, **kwargs)