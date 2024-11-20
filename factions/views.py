from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game, Session, Event, Faction, Project, ProjectChange
from .forms import GameForm, ProjectForm
from django.urls import reverse_lazy, reverse
from django.db.models import Sum
import yaml
import os
from django.contrib import messages
from .utils import load_yaml_file

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

# Sessions
class SessionListView(ListView):
    model = Session
    template_name = 'session/session_list.html'
    context_object_name = 'sessions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = Game.objects.get(id=self.kwargs['game_id'])
        context['game'] = game
        return context

    def get_queryset(self):
        sessions = Session.objects.filter(game_id=self.kwargs['game_id']).order_by('-when')
        return sessions

class SessionCreateView(CreateView):
    model = Session
    template_name = 'session/session_form.html'
    fields = ['name', 'description', 'when']

    def form_valid(self, form):
        form.instance.game_id = self.kwargs['game_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('session_list', kwargs={'game_id': self.kwargs['game_id']})

class SessionDetailView(DetailView):
    model = Session
    template_name = 'session/session_detail.html'
    context_object_name = 'session'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.object.game
        return context

# Events
class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = Game.objects.get(id=self.kwargs['game_id'])
        context['game'] = game
        return context

    def get_queryset(self):
        events = Event.objects.filter(game_id=self.kwargs['game_id']).order_by('-when')
        return events

class EventCreateView(CreateView):
    model = Event
    template_name = 'event/event_form.html'
    fields = ['name', 'description', 'when']

    def form_valid(self, form):
        form.instance.game_id = self.kwargs['game_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('event_list', kwargs={'game_id': self.kwargs['game_id']})

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.object.game
        return context

# Projects
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

# Import Test Data
def import_test_data(request):
    data_directory = os.path.join(os.path.dirname(__file__), 'data')

    # Import Games
    game_directory = os.path.join(data_directory, 'game')
    if os.path.exists(game_directory):
        for filename in os.listdir(game_directory):
            if filename.endswith('.yaml'):
                file_path = os.path.join(game_directory, filename)
                data = load_yaml_file(file_path)

                if isinstance(data, list):
                    for item_data in data:
                        Game.objects.update_or_create(
                            name=item_data['name'],
                            defaults={
                                'description': item_data.get('description', ''),
                            }
                        )
                else:
                    Game.objects.update_or_create(
                        name=data['name'],
                        defaults={
                            'description': data.get('description', ''),
                        }
                    )

    # Import Factions
    faction_directory = os.path.join(data_directory, 'faction')
    if os.path.exists(faction_directory):
        for filename in os.listdir(faction_directory):
            if filename.endswith('.yaml'):
                file_path = os.path.join(faction_directory, filename)
                data = load_yaml_file(file_path)

                if isinstance(data, list):
                    for item_data in data:
                        game_name = item_data.pop('game', None)
                        game = Game.objects.get(name=game_name) if game_name else None

                        Faction.objects.update_or_create(
                            name=item_data['name'],
                            game=game,
                            defaults={
                                'description': item_data.get('description', ''),
                                'tier': item_data.get('tier', 0),
                                'goals': item_data.get('goals', ''),
                                'leadership': item_data.get('leadership', ''),
                                'values': item_data.get('values', ''),
                                'history': item_data.get('history', ''),
                            }
                        )
                else:
                    game_name = data.pop('game', None)
                    game = Game.objects.get(name=game_name) if game_name else None

                    Faction.objects.update_or_create(
                        name=data['name'],
                        game=game,
                        defaults={
                            'description': data.get('description', ''),
                            'tier': data.get('tier', 0),
                            'goals': data.get('goals', ''),
                            'leadership': data.get('leadership', ''),
                            'values': data.get('values', ''),
                            'history': data.get('history', ''),
                        }
                    )

    # Import Projects
    project_directory = os.path.join(data_directory, 'project')
    if os.path.exists(project_directory):
        for filename in os.listdir(project_directory):
            if filename.endswith('.yaml'):
                file_path = os.path.join(project_directory, filename)
                data = load_yaml_file(file_path)

                if isinstance(data, list):
                    for item_data in data:
                        game_name = item_data.pop('game', None)
                        game = Game.objects.get(name=game_name) if game_name else None

                        faction_names = item_data.pop('factions', [])
                        factions = Faction.objects.filter(name__in=faction_names, game=game)

                        project, created = Project.objects.update_or_create(
                            name=item_data['name'],
                            game=game,
                            defaults={
                                'description': item_data.get('description', ''),
                                'length': item_data.get('length', 4),
                                'finished': item_data.get('finished', None),
                            }
                        )
                        project.factions.set(factions)
                else:
                    game_name = data.pop('game', None)
                    game = Game.objects.get(name=game_name) if game_name else None

                    faction_names = data.pop('factions', [])
                    factions = Faction.objects.filter(name__in=faction_names, game=game)

                    project, created = Project.objects.update_or_create(
                        name=data['name'],
                        game=game,
                        defaults={
                            'description': data.get('description', ''),
                            'length': data.get('length', 4),
                            'finished': data.get('finished', None),
                        }
                    )
                    project.factions.set(factions)

    # Import Sessions
    session_directory = os.path.join(data_directory, 'session')
    if os.path.exists(session_directory):
        for filename in os.listdir(session_directory):
            if filename.endswith('.yaml'):
                file_path = os.path.join(session_directory, filename)
                data = load_yaml_file(file_path)

                if isinstance(data, list):
                    for item_data in data:
                        game_name = item_data.pop('game', None)
                        game = Game.objects.get(name=game_name) if game_name else None

                        Session.objects.update_or_create(
                            name=item_data['name'],
                            game=game,
                            when=item_data.get('when', 0),
                            defaults={
                                'description': item_data.get('description', ''),
                            }
                        )
                else:
                    game_name = data.pop('game', None)
                    game = Game.objects.get(name=game_name) if game_name else None

                    Session.objects.update_or_create(
                        name=data['name'],
                        game=game,
                        when=data.get('when', 0),
                        defaults={
                            'description': data.get('description', ''),
                        }
                    )

    # Import Events
    event_directory = os.path.join(data_directory, 'event')
    if os.path.exists(event_directory):
        for filename in os.listdir(event_directory):
            if filename.endswith('.yaml'):
                file_path = os.path.join(event_directory, filename)
                data = load_yaml_file(file_path)

                if isinstance(data, list):
                    for item_data in data:
                        game_name = item_data.pop('game', None)
                        game = Game.objects.get(name=game_name) if game_name else None

                        Event.objects.update_or_create(
                            name=item_data['name'],
                            game=game,
                            when=item_data.get('when', 0),
                            defaults={
                                'description': item_data.get('description', ''),
                            }
                        )
                else:
                    game_name = data.pop('game', None)
                    game = Game.objects.get(name=game_name) if game_name else None

                    Event.objects.update_or_create(
                        name=data['name'],
                        game=game,
                        when=data.get('when', 0),
                        defaults={
                            'description': data.get('description', ''),
                        }
                    )

    # Import ProjectChanges
    project_change_directory = os.path.join(data_directory, 'projectchange')
    if os.path.exists(project_change_directory):
        for filename in os.listdir(project_change_directory):
            if filename.endswith('.yaml'):
                file_path = os.path.join(project_change_directory, filename)
                data = load_yaml_file(file_path)

                if isinstance(data, list):
                    for item_data in data:
                        project_name = item_data.pop('project', None)
                        event_name = item_data.pop('event', None)
                        game_name = item_data.pop('game', None)

                        game = Game.objects.get(name=game_name) if game_name else None
                        project = Project.objects.get(name=project_name, game=game)
                        event = Event.objects.get(name=event_name, game=game)

                        ProjectChange.objects.update_or_create(
                            project=project,
                            event=event,
                            defaults={
                                'amount': item_data.get('amount', 0),
                            }
                        )
                else:
                    project_name = data.pop('project', None)
                    event_name = data.pop('event', None)
                    game_name = data.pop('game', None)

                    game = Game.objects.get(name=game_name) if game_name else None
                    project = Project.objects.get(name=project_name, game=game)
                    event = Event.objects.get(name=event_name, game=game)

                    ProjectChange.objects.update_or_create(
                        project=project,
                        event=event,
                        defaults={
                            'amount': data.get('amount', 0),
                        }
                    )

    messages.success(request, 'Successfully imported test data.')
    return redirect('game_list')
