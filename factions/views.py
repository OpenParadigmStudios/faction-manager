from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Timeline, Session, Event, Faction, Project, Clock, ClockChange
from .forms import TimelineForm, ProjectForm
from django.urls import reverse_lazy, reverse
from django.db.models import Sum

# Timelines
class TimelineListView(ListView):
    model = Timeline
    template_name = 'timeline/timeline_list.html'
    context_object_name = 'timelines'

class TimelineDetailView(DetailView):
    model = Timeline
    template_name = 'timeline/timeline_detail.html'
    context_object_name = 'timeline'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timeline = self.object

        # Using model helper methods to get the dynamic data
        context['latest_sessions'] = timeline.latest_sessions()
        context['latest_events'] = timeline.latest_events()
        context['top_factions'] = timeline.top_factions()
        context['top_projects'] = timeline.top_projects()
        context['now'] = timeline.now()
        return context

class TimelineCreateView(CreateView):
    model = Timeline
    fields = ['name', 'description']
    template_name = 'timeline/timeline_form.html'
    success_url = reverse_lazy('timeline_list')

class TimelineUpdateView(UpdateView):
    model = Timeline
    fields = ['name', 'description']
    template_name = 'timeline/timeline_form.html'
    success_url = reverse_lazy('timeline_list')

    def form_valid(self, form):
        # Implementing deletion functionality
        if "delete" in self.request.POST:
            self.object.delete()
            return redirect(self.success_url)
        return super().form_valid(form)

class TimelineDeleteView(DeleteView):
    model = Timeline
    template_name = 'timeline/timeline_confirm_delete.html'
    success_url = reverse_lazy('timeline_list')

# Factions
class FactionListView(ListView):
    model = Faction
    template_name = 'faction/faction_list.html'
    context_object_name = 'factions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = Timeline.objects.get(id=self.kwargs['timeline_id'])
        return context

    def get_queryset(self):
        factions = Faction.objects.filter(timeline_id=self.kwargs['timeline_id'])
        factions = factions.annotate(total_clock_length=Sum('projects__clocks__length'))
        factions = factions.order_by('-total_clock_length')
        return factions

class FactionDetailView(DetailView):
    model = Faction
    template_name = 'faction/faction_detail.html'
    context_object_name = 'faction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = Timeline.objects.get(id=self.kwargs['timeline_id'])
        # Add recent events
        context['recent_events'] = self.get_recent_events()
        return context

    def get_recent_events(self):
        faction = self.get_object()
        recent_events = Event.objects.filter(
            clock_changes__clock__project__factions=faction
        ).distinct().order_by('-when')[:5]
        return recent_events

class FactionCreateView(CreateView):
    model = Faction
    fields = ['name', 'description', 'tier', 'goals', 'leadership', 'values', 'history']
    template_name = 'faction/faction_form.html'

    def get_success_url(self):
        return reverse('faction_list', kwargs={'timeline_id': self.kwargs['timeline_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = Timeline.objects.get(id=self.kwargs['timeline_id'])
        return context

    def form_valid(self, form):
        form.instance.timeline_id = self.kwargs['timeline_id']
        return super().form_valid(form)

class FactionUpdateView(UpdateView):
    model = Faction
    fields = ['name', 'description', 'tier', 'goals', 'leadership', 'values', 'history']
    template_name = 'faction/faction_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = Timeline.objects.get(id=self.kwargs['timeline_id'])
        return context

    def form_valid(self, form):
        form.instance.timeline_id = self.kwargs['timeline_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('faction_list', kwargs={'timeline_id': self.kwargs['timeline_id']})

class FactionDeleteView(DeleteView):
    model = Faction
    template_name = 'faction/faction_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = Timeline.objects.get(id=self.kwargs['timeline_id'])
        return context

    def get_success_url(self):
        return reverse('faction_list', kwargs={'timeline_id': self.kwargs['timeline_id']})

# Placeholder Session Views
class SessionListView(ListView):
    model = Session
    template_name = 'session/session_list.html'
    context_object_name = 'sessions'

class SessionCreateView(CreateView):
    model = Session
    template_name = 'session/session_form.html'
    fields = ['name', 'description', 'when']

class SessionDetailView(DetailView):
    model = Session
    template_name = 'session/session_detail.html'
    context_object_name = 'session'

# Placeholder Event Views
class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Event
    template_name = 'event/event_form.html'
    fields = ['name', 'description', 'when']

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'

# Project Views
class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        timeline = get_object_or_404(Timeline, id=self.kwargs['timeline_id'])
        projects = Project.objects.filter(timeline=timeline)
        # Filter by Faction if provided
        faction_id = self.request.GET.get('faction')
        if faction_id:
            projects = projects.filter(factions__id=faction_id)
        # Filter by completed status
        show_completed = self.request.GET.get('show_completed', 'on')
        if show_completed != 'on':
            projects = projects.exclude(clocks__finished__gt=0)
        # Annotate with progress percentage
        projects = list(projects.distinct())
        projects.sort(key=lambda p: p.progress_percentage(), reverse=True)
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timeline = get_object_or_404(Timeline, id=self.kwargs['timeline_id'])
        context['timeline'] = timeline
        context['factions'] = Faction.objects.filter(timeline=timeline)
        context['selected_faction'] = self.request.GET.get('faction', '')
        context['show_completed'] = self.request.GET.get('show_completed', 'on')
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['timeline'] = project.timeline
        # Calculate progress
        context['progress_percentage'] = project.progress_percentage()
        # Get all events affecting the project's clocks
        events = Event.objects.filter(
            clock_changes__clock__in=project.clocks.all()
        ).distinct().order_by('-when')
        context['events'] = events
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk, 'timeline_id': self.object.timeline.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timeline = Timeline.objects.get(id=self.kwargs['timeline_id'])
        context['timeline'] = timeline
        context['factions'] = Faction.objects.filter(timeline=timeline)
        # Pre-select faction if passed in URL
        faction_id = self.request.GET.get('faction_id')
        if faction_id:
            context['form'].fields['factions'].initial = [faction_id]
        return context

    def form_valid(self, form):
        timeline = Timeline.objects.get(id=self.kwargs['timeline_id'])
        form.instance.timeline = timeline
        response = super().form_valid(form)
        # Associate factions
        factions = form.cleaned_data.get('factions')
        if factions:
            form.instance.factions.set(factions)
        else:
            form.instance.factions.clear()
        # Create the Clock
        clock_length = form.cleaned_data.get('clock_length')
        Clock.objects.create(
            project=self.object,
            length=clock_length,
            title=form.instance.name
        )
        return response

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk, 'timeline_id': self.object.timeline.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timeline = self.object.timeline
        context['timeline'] = timeline
        context['factions'] = Faction.objects.filter(timeline=timeline)
        return context

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'

    def get_success_url(self):
        return reverse('project_list', kwargs={'timeline_id': self.object.timeline.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = self.object.timeline
        return context

# Placeholder Clock Views
class ClockListView(ListView):
    model = Clock
    template_name = 'clock/clock_list.html'
    context_object_name = 'clocks'

class ClockCreateView(CreateView):
    model = Clock
    template_name = 'clock/clock_form.html'
    fields = ['title']

class ClockDetailView(DetailView):
    model = Clock
    template_name = 'clock/clock_detail.html'
    context_object_name = 'clock'

# Placeholder ClockChange Views
class ClockChangeListView(ListView):
    model = ClockChange
    template_name = 'clockchange/clockchange_list.html'
    context_object_name = 'clockchanges'

class ClockChangeCreateView(CreateView):
    model = ClockChange
    template_name = 'clockchange/clockchange_form.html'
    fields = ['name', 'description']

class ClockChangeDetailView(DetailView):
    model = ClockChange
    template_name = 'clockchange/clockchange_detail.html'
    context_object_name = 'clockchange'
