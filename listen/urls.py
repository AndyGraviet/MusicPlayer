from .views  import listenPageView
from django.urls import path

app_name = 'listen'

urlpatterns = [
    path("", listenPageView, name='base')
]
