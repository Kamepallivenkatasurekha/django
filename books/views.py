from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetriveUpdateDestroyAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer