from django.urls import path
from .views import *

urlpatterns = [
     path("flames/", flames_view, name='flames'),
]
