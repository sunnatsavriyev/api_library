from django.urls import path
from .views import BookApiView, BookDetail

urlpatterns = [
    path('',BookApiView.as_view()),
    path("<int:pk>/",BookDetail.as_view())
]
