from django.contrib import admin
from .models import Game, Session, Faction, Project, Event, ProjectChange

admin.site.register(Game)
admin.site.register(Session)
admin.site.register(Faction)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(ProjectChange)
