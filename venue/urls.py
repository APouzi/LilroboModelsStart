from django.urls.conf import path
from . import views

urlpatterns = [
    path('venue', views.venue, name = 'venue'),
]