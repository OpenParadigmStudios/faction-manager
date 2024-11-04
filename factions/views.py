from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Timeline, Faction
from django.urls import reverse_lazy

# Timelines
class TimelineListView(ListView):
    model = Timeline
    template_name = 'timeline/timeline_list.html'
    context_object_name = 'timelines'

class TimelineDetailView(DetailView):
    model = Timeline
    template_name = 'timeline/timeline_detail.html'
    context_object_name = 'timeline'

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
        return Faction.objects.filter(timeline_id=self.kwargs['timeline_id'])

class FactionDetailView(DetailView):
    model = Faction
    template_name = 'faction/faction_detail.html'
    context_object_name = 'faction'

class FactionCreateView(CreateView):
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
        return reverse_lazy('faction_list', kwargs={'timeline_id': self.kwargs['timeline_id']})

class FactionUpdateView(UpdateView):
    model = Faction
    fields = ['name', 'description', 'tier', 'goals', 'leadership', 'values', 'history']
    template_name = 'faction/faction_form.html'

    def get_success_url(self):
        return reverse_lazy('faction_list', kwargs={'timeline_id': self.object.timeline.id})

class FactionDeleteView(DeleteView):
    model = Faction
    template_name = 'faction/faction_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('faction_list', kwargs={'timeline_id': self.object.timeline.id})

