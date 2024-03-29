from django.urls import path

from .views import produceMessage

urlpatterns = [
    path('produceMessage', produceMessage)
]