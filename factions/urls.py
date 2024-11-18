from django.urls import path
from . import views

urlpatterns = [
    # Timeline URLs
    path('timelines/', views.TimelineListView.as_view(), name='timeline_list'),
    path('timelines/<int:pk>/', views.TimelineDetailView.as_view(), name='timeline_detail'),
    path('timelines/create/', views.TimelineCreateView.as_view(), name='timeline_create'),
    path('timelines/<int:pk>/edit/', views.TimelineUpdateView.as_view(), name='timeline_edit'),

    path('sessions/<int:timeline_id>', views.SessionListView.as_view(), name='session_list'),
    path('sessions/create/<int:timeline_id>', views.SessionCreateView.as_view(), name='session_create'),
    path('sessions/<int:pk>/<int:timeline_id>', views.SessionDetailView.as_view(), name='session_detail'),

    path('events/<int:timeline_id>', views.EventListView.as_view(), name='event_list'),
    path('events/create/<int:timeline_id>', views.EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/<int:timeline_id>', views.EventDetailView.as_view(), name='event_detail'),

    path('factions/<int:timeline_id>', views.FactionListView.as_view(), name='faction_list'),
    path('factions/create/<int:timeline_id>', views.FactionCreateView.as_view(), name='faction_create'),
    path('factions/<int:pk>/<int:timeline_id>', views.FactionDetailView.as_view(), name='faction_detail'),
    path('factions/edit/<int:pk>/<int:timeline_id>', views.FactionUpdateView.as_view(), name='faction_update'),
    path('factions/delete/<int:pk>/<int:timeline_id>', views.FactionDeleteView.as_view(), name='faction_delete'),

    path('projects/<int:timeline_id>/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/create/<int:timeline_id>/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/<int:timeline_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/edit/<int:pk>/<int:timeline_id>/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/delete/<int:pk>/<int:timeline_id>/', views.ProjectDeleteView.as_view(), name='project_delete'),

    path('clocks/<int:timeline_id>', views.ClockListView.as_view(), name='clock_list'),
    path('clocks/create/<int:timeline_id>', views.ClockCreateView.as_view(), name='clock_create'),
    path('clocks/<int:pk>/<int:timeline_id>', views.ClockDetailView.as_view(), name='clock_detail'),

    path('clockchanges/<int:timeline_id>', views.ClockChangeListView.as_view(), name='clockchange_list'),
    path('clockchanges/create/<int:timeline_id>', views.ClockChangeCreateView.as_view(), name='clockchange_create'),
    path('clockchanges/<int:pk>/<int:timeline_id>', views.ClockChangeDetailView.as_view(), name='clockchange_detail'),
]
