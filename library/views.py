from django.shortcuts import render
from django.views.generic import ListView
from .models import Books
# Create your views here.

#eSTE SI
class ListBook(ListView):

    model=Books
    template_name="booklist.html"

    