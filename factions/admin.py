from django.contrib import admin
from .models import Timeline, Session, Faction, Project, Clock, Event, ClockChange

admin.site.register(Timeline)
admin.site.register(Session)
admin.site.register(Faction)
admin.site.register(Project)
admin.site.register(Clock)
admin.site.register(Event)
admin.site.register(ClockChange)
