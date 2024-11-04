from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Timeline
from django.urls import reverse_lazy

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
