from django.shortcuts import render

# Create your views here.

from .models import Book
from .seriazlizers import BookSerializer
from rest_framework import generics

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer