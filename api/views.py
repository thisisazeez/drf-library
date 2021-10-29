from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from books.models import Books
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
