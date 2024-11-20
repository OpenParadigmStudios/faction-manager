from django.db import models
from django.db.models import Max, Sum, F

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def now(self):
        """Calculate the current time 'Now' by finding the max 'When' from sessions in this game."""
        latest_session = self.sessions.order_by('-when').first()
        return latest_session.when if latest_session else 0

    def latest_sessions(self, limit=5):
        """Return the latest sessions ordered by 'When' descending."""
        return self.sessions.order_by('-when')[:limit]

    def latest_events(self, limit=5):
        """Return the latest events ordered by 'When' descending."""
        return Event.objects.filter(game=self).order_by('-when')[:limit]

    def top_factions(self, limit=5):
        """Return the top factions based on the total length of all projects."""
        return Faction.objects.filter(game=self).annotate(
            total_project_length=Sum('projects__length')
        ).order_by('-total_project_length')[:limit]

    def top_projects(self, limit=5):
        """Return the top projects sorted by their progress percentage."""
        projects = list(self.projects.all())
        projects.sort(key=lambda project: project.progress_percentage(), reverse=True)
        return projects[:limit]

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    when = models.IntegerField()
    game = models.ForeignKey(Game, related_name='sessions', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} (When: {self.when})"

class Faction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tier = models.IntegerField()
    goals = models.TextField()
    leadership = models.TextField()
    values = models.TextField()
    history = models.TextField()
    game = models.ForeignKey(Game, related_name='factions', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def active_projects(self):
        # Return projects where all clocks are not finished
        return self.projects.filter(finished__isnull=True).distinct()

    def completed_projects(self):
        # Return projects where all clocks are finished
        return self.projects.filter(finished__isnull=False).distinct()
    
    def total_clock_length(self):
        return self.projects.aggregate(total_length=Sum('length'))['total_length'] or 0

    def recent_events(self, limit=5):
        return Event.objects.filter(
            project_changes__project__factions=self
        ).distinct().order_by('-when')[:limit]

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    game = models.ForeignKey(Game, related_name='projects', on_delete=models.CASCADE)
    factions = models.ManyToManyField(Faction, related_name='projects')
    length = models.PositiveIntegerField(default=4)
    finished = models.IntegerField(null=True, blank=True, default=None)  # Allow NULL values
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def progress_percentage(self):
        """Calculate the project’s progress as a percentage."""
        total_length = self.length or 1
        total_progress = self.calculate_progress()
        return (total_progress / total_length) * 100

    def calculate_progress(self):
        """Calculate the current progress of the project by summing related ProjectChange amounts."""
        return self.changes.aggregate(total_progress=Sum('amount'))['total_progress'] or 0

    def check_if_finished(self):
        """Mark the project as finished if progress meets or exceeds its length."""
        if self.calculate_progress() >= self.length and self.finished is None:
            latest_change = self.changes.order_by('-event__when').first()
            self.finished = latest_change.event.when if latest_change else 1
            self.save()

    def is_finished(self):
        """Check if the project is finished."""
        return self.finished is not None

    def __str__(self):
        return f"{self.name} ({self.calculate_progress()}/{self.length})"

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    when = models.IntegerField()
    game = models.ForeignKey(Game, related_name='events', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} (When: {self.when})"

class ProjectChange(models.Model):
    project = models.ForeignKey('Project', related_name='changes', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='project_changes', on_delete=models.CASCADE)
    amount = models.IntegerField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Change of {self.amount} to {self.project.name}"
