from django.urls import path
from .views import TimelineListView, TimelineDetailView, TimelineCreateView, TimelineUpdateView, TimelineDeleteView

urlpatterns = [
    path('timelines/', TimelineListView.as_view(), name='timeline_list'),
    path('timelines/<int:pk>/', TimelineDetailView.as_view(), name='timeline_detail'),
    path('timelines/create/', TimelineCreateView.as_view(), name='timeline_create'),
    path('timelines/<int:pk>/edit/', TimelineUpdateView.as_view(), name='timeline_update'),
    path('timelines/<int:pk>/delete/', TimelineDeleteView.as_view(), name='timeline_delete'),
]
