from .views import listen
from django.urls import path

urlpatterns = [
    path("", listen)
]
