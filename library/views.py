from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Set


class SetListView(generic.ListView):
    model = Set
    template_name = 'index.html'
    paginate_by = 4


def search(request):
    """ search function  """
    if request.method == "POST":
        searched = request.POST['searched']
        sets = Set.objects.filter(theme__contains=searched)

        return render(request, 'search.html', {'searched': searched, 
        'sets': sets})
    else: 
        return render(request, 'search.html', {})
