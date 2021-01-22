from django.shortcuts import render
from .models import SomeList
from django.views.generic import ListView


# Create your views here.
class SomeListView(ListView):
    template_name = "some-list.html"
    model = SomeList