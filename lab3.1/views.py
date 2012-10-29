# Create your views here.

from library.models import Book
from library.models import Author
from library.models import Publisher
from django.shortcuts import render

def booklist(request, sub):
    books = Book.objects.all()
    d = {'books':books}
    return render(request, 'booklist.html', d)

def bookinfo(request, sub):
    book = Book.objects.get(id=sub)
    d = {'book':book, 'authors': book.authors.all()}
    return render(request, 'bookinfo.html', d)




