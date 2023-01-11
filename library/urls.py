from . import views
from django.urls import path

urlpatterns = [
    path('', views.SetListView.as_view(), name='home')
]