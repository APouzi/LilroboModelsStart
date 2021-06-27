from django.db.models.fields.related import ForeignKey
from django.db import models
from performer.models import Performer
from venue.models import Venue

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    #Do we want to do an "on_delete = models.DO_NOTHING"?
    performer = models.ForeignKey(Performer, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=1000)
    capacity = models.IntegerField()
    date = models.DateTimeField(blank =True)
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING, blank = True)
    
    # EventFlyer how we going to do the image?
    
    # Here we talked about "created_by". for this, we are going to have to talk about Users and how we want to handle accounts, for now, I will leave this as a textfield
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name

