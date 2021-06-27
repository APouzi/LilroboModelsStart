from django.urls.conf import path
from . import views

urlpatterns = [
    path('events', views.events, name = 'events'),
    path('event',views.event, name = 'event')
]