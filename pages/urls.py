from django.urls.conf import path
from . import views
# Create your tests here.

urlpatterns = [
    path('', views.index, name = 'index'),
]