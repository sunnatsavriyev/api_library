from django.urls import path
from .views import BookView


urlpatterns = [
    path('',BookView,name='home')
]
