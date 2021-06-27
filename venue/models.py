from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length = 200, blank= True)  
    street = models.CharField(max_length = 200, blank= True)    
    city = models.CharField(max_length = 200, blank= True)
    state = models.CharField(max_length = 100, blank= True)
    country = models.CharField(max_length= 100, blank= True)
    zipcode = models.CharField(max_length = 20, blank= True)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6, blank= True)
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6, blank= True)
    def __str__(self):
        return self.venue_name