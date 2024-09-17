from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from config.models import Book
from .serializers import BookSerializer
from rest_framework import permissions
# Create your views here.

class BookApiView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer