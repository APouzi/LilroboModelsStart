from django.db import models

# Create your models here.
class Performer(models.Model):
    first_name = models.CharField(max_length = 200, blank= True)
    last_name = models.CharField(max_length = 200, blank= True)
    stage_name = models.CharField(max_length = 200, )
    email = models.CharField(max_length = 200, blank= True)
    street = models.CharField(max_length = 200, blank= True)
    city = models.CharField(max_length = 200, blank= True)
    state = models.CharField(max_length = 100, blank= True)
    country = models.CharField(max_length= 100, blank= True)
    zipcode = models.CharField(max_length = 20, blank= True)
    based_from = models.CharField(max_length = 200, blank= True)
    genre = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.stage_name
    
