from django.http import request
from django.shortcuts import render
from .models import Book
from django import views
# Create your views here.


def BookView(request):
    book=Book.objects.all()


    ctx={
        'book': book
    }
        
    
    return render (request, 'index.html', ctx)
