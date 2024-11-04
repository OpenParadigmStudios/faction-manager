from django.urls import path
from .views import (TimelineListView, TimelineDetailView, TimelineCreateView, TimelineUpdateView, TimelineDeleteView,
                    FactionListView, FactionDetailView, FactionCreateView, FactionUpdateView, FactionDeleteView)

urlpatterns = [
    # Timeline URLs
    path('timelines/', TimelineListView.as_view(), name='timeline_list'),
    path('timelines/<int:pk>/', TimelineDetailView.as_view(), name='timeline_detail'),
    path('timelines/create/', TimelineCreateView.as_view(), name='timeline_create'),
    path('timelines/<int:pk>/edit/', TimelineUpdateView.as_view(), name='timeline_update'),
    path('timelines/<int:pk>/delete/', TimelineDeleteView.as_view(), name='timeline_delete'),

    # Faction URLs
    path('timelines/<int:timeline_id>/factions/', FactionListView.as_view(), name='faction_list'),
    path('timelines/<int:timeline_id>/factions/<int:pk>/', FactionDetailView.as_view(), name='faction_detail'),
    path('timelines/<int:timeline_id>/factions/create/', FactionCreateView.as_view(), name='faction_create'),
    path('timelines/<int:timeline_id>/factions/<int:pk>/edit/', FactionUpdateView.as_view(), name='faction_update'),
    path('timelines/<int:timeline_id>/factions/<int:pk>/delete/', FactionDeleteView.as_view(), name='faction_delete'),
]
