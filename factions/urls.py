from django.urls import path
from . import views

urlpatterns = [
    # Game URLs
    path('games/', views.GameListView.as_view(), name='game_list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('games/create/', views.GameCreateView.as_view(), name='game_create'),
    path('games/<int:pk>/edit/', views.GameUpdateView.as_view(), name='game_edit'),

    path('sessions/<int:game_id>', views.SessionListView.as_view(), name='session_list'),
    path('sessions/create/<int:game_id>', views.SessionCreateView.as_view(), name='session_create'),
    path('sessions/<int:pk>/<int:game_id>', views.SessionDetailView.as_view(), name='session_detail'),

    path('events/<int:game_id>', views.EventListView.as_view(), name='event_list'),
    path('events/create/<int:game_id>', views.EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/<int:game_id>', views.EventDetailView.as_view(), name='event_detail'),

    path('factions/<int:game_id>', views.FactionListView.as_view(), name='faction_list'),
    path('factions/create/<int:game_id>', views.FactionCreateView.as_view(), name='faction_create'),
    path('factions/<int:pk>/<int:game_id>', views.FactionDetailView.as_view(), name='faction_detail'),
    path('factions/edit/<int:pk>/<int:game_id>', views.FactionUpdateView.as_view(), name='faction_update'),
    path('factions/delete/<int:pk>/<int:game_id>', views.FactionDeleteView.as_view(), name='faction_delete'),

    path('projects/<int:game_id>/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/create/<int:game_id>/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/<int:game_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/edit/<int:pk>/<int:game_id>/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/delete/<int:pk>/<int:game_id>/', views.ProjectDeleteView.as_view(), name='project_delete'),

    # Removed Clock and ClockChange URLs as Clocks are no longer used
]
