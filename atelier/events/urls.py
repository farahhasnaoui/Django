from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     path('eventslist/', ListEvent ,name="list_events"),
     path('addevent/', ListEvent ,name="add_event"),
     path('eventslistView/' , ListEventView.as_view(),name='list_events_view') ,
     path('eventDetails/<int:pk>',DetailEventView.as_view(),name='detailsevent')
]
