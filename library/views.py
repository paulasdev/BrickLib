from django.shortcuts import render
from django.views import generic
from .models import Set


class SetListView(generic.ListView):
    model = Set
    template_name = 'index.html'
    paginate_by = 4