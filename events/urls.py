from django.urls import path
from .views import EventListCreateView, EventDetailView, TicketListCreateView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
]
