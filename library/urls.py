from . import views
from django.urls import path

urlpatterns = [
    path('', views.SetListView.as_view(), name='home')
    path('search', views.search, name='search_results'),
]