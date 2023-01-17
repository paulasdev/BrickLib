from . import views
from django.urls import path

urlpatterns = [
    path('', views.SetListView.as_view(), name='home'),
    path('search', views.search, name='search_results'),
    path('add_set', views.add_set, name='add_set'),
    path('set_list', views.set_list, name='set_list'),
    path('lego-set/<str:id>', views.show_set.as_view(), name='show_set'),
]