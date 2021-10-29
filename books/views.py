from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import Books


class BookListView(ListView):
    model = Books
    template_name = 'books_list.html'
