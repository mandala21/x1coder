from .views import ChallegenListCreateView
from django.urls import path

app_name = 'challegen'

urlpatterns = [
    path('',ChallegenListCreateView.as_view(),name='challegen.index'),
]