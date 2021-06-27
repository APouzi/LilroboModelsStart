from django.urls.conf import path
from . import views

urlpatterns = [
    path('performers', views.performers, name = 'performers'),
    path('performer', views.performer, name = 'performer')
]