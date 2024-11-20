from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game, Session, Event, Faction, Project  # Removed Clock, ClockChange
from .forms import GameForm, ProjectForm
from django.urls import reverse_lazy, reverse
from django.db.models import Sum

# Games
class GameListView(ListView):
    model = Game
    template_name = 'game/game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name = 'game/game_detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.object

        # Using model helper methods to get the dynamic data
        context['latest_sessions'] = game.latest_sessions()
        context['latest_events'] = game.latest_events()
        context['top_factions'] = game.top_factions()
        context['top_projects'] = game.top_projects()
        context['now'] = game.now()
        return context

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'description']
    template_name = 'game/game_form.html'
    success_url = reverse_lazy('game_list')

class GameUpdateView(UpdateView):
    model = Game
    fields = ['name', 'description']
    template_name = 'game/game_form.html'
    success_url = reverse_lazy('game_list')

    def form_valid(self, form):
        # Implementing deletion functionality
        if "delete" in self.request.POST:
            self.object.delete()
            return redirect(self.success_url)
        return super().form_valid(form)

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'game/game_confirm_delete.html'
    success_url = reverse_lazy('game_list')

# Factions
class FactionListView(ListView):
    model = Faction
    template_name = 'faction/faction_list.html'
    context_object_name = 'factions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(id=self.kwargs['game_id'])
        return context

    def get_queryset(self):
        factions = Faction.objects.filter(game_id=self.kwargs['game_id'])
        factions = factions.annotate(total_project_length=Sum('projects__length'))
        factions = factions.order_by('-total_project_length')
        return factions

class FactionDetailView(DetailView):
    model = Faction
    template_name = 'faction/faction_detail.html'
    context_object_name = 'faction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(id=self.kwargs['game_id'])
        # Add recent events
        context['recent_events'] = self.get_recent_events()
        return context

    def get_recent_events(self):
        faction = self.get_object()
        recent_events = Event.objects.filter(
            project_changes__project__factions=faction
        ).distinct().order_by('-when')[:5]
        return recent_events

class FactionCreateView(CreateView):
    model = Faction
    fields = ['name', 'description', 'tier', 'goals', 'leadership', 'values', 'history']
    template_name = 'faction/faction_form.html'

    def get_success_url(self):
        return reverse('faction_list', kwargs={'game_id': self.kwargs['game_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(id=self.kwargs['game_id'])
        return context

    def form_valid(self, form):
        form.instance.game_id = self.kwargs['game_id']
        return super().form_valid(form)

class FactionUpdateView(UpdateView):
    model = Faction
    fields = ['name', 'description', 'tier', 'goals', 'leadership', 'values', 'history']
    template_name = 'faction/faction_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(id=self.kwargs['game_id'])
        return context

    def form_valid(self, form):
        form.instance.game_id = self.kwargs['game_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('faction_list', kwargs={'game_id': self.kwargs['game_id']})

class FactionDeleteView(DeleteView):
    model = Faction
    template_name = 'faction/faction_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(id=self.kwargs['game_id'])
        return context

    def get_success_url(self):
        return reverse('faction_list', kwargs={'game_id': self.kwargs['game_id']})

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
        game = get_object_or_404(Game, id=self.kwargs['game_id'])
        projects = Project.objects.filter(game=game)
        # Filter by Faction if provided
        faction_id = self.request.GET.get('faction')
        if faction_id:
            projects = projects.filter(factions__id=faction_id)
        # Filter by completed status
        show_completed = self.request.GET.get('show_completed', 'on')
        if show_completed != 'on':
            projects = projects.filter(finished__isnull=True)
        # Annotate with progress percentage
        projects = list(projects.distinct())
        projects.sort(key=lambda p: p.progress_percentage(), reverse=True)
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = get_object_or_404(Game, id=self.kwargs['game_id'])
        context['game'] = game
        context['factions'] = Faction.objects.filter(game=game)
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
        context['game'] = project.game
        # Calculate progress
        context['progress_percentage'] = project.progress_percentage()
        # Get all events affecting the project
        events = Event.objects.filter(
            project_changes__project=project
        ).distinct().order_by('-when')
        context['events'] = events
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk, 'game_id': self.object.game.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = Game.objects.get(id=self.kwargs['game_id'])
        context['game'] = game
        context['factions'] = Faction.objects.filter(game=game)
        # Pre-select faction if passed in URL
        faction_id = self.request.GET.get('faction_id')
        if faction_id:
            context['form'].fields['factions'].initial = [faction_id]
        return context

    def form_valid(self, form):
        game = Game.objects.get(id=self.kwargs['game_id'])
        form.instance.game = game
        response = super().form_valid(form)
        # Associate factions
        factions = form.cleaned_data.get('factions')
        if factions:
            form.instance.factions.set(factions)
        else:
            form.instance.factions.clear()
        return response

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk, 'game_id': self.object.game.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.object.game
        context['game'] = game
        context['factions'] = Faction.objects.filter(game=game)
        return context

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'

    def get_success_url(self):
        return reverse('project_list', kwargs={'game_id': self.object.game.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.object.game
        return context
