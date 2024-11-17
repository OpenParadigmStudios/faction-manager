from django.db import models
from django.db.models import Max, Sum, F

class Timeline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def now(self):
        """Calculate the current time 'Now' by finding the max 'When' from sessions in this timeline."""
        latest_session = self.sessions.order_by('-when').first()
        return latest_session.when if latest_session else 0

    def latest_sessions(self, limit=5):
        """Return the latest sessions ordered by 'When' descending."""
        return self.sessions.order_by('-when')[:limit]

    def latest_events(self, limit=5):
        """Return the latest events ordered by 'When' descending."""
        return Event.objects.filter(timeline=self).order_by('-when')[:limit]

    def top_factions(self, limit=5):
        """Return the top factions based on the total length of all clocks in their projects."""
        return Faction.objects.filter(timeline=self).annotate(
            total_project_length=Sum('projects__clocks__length')
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
    timeline = models.ForeignKey(Timeline, related_name='sessions', on_delete=models.CASCADE)
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
    timeline = models.ForeignKey(Timeline, related_name='factions', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def active_projects(self):
        return self.projects.filter(clocks__finished__isnull=True).distinct()
    
    def completed_projects(self):
        return self.projects.filter(clocks__finished__isnull=False).distinct()
    

    def total_clock_length(self):
        return self.projects.aggregate(total_length=Sum('clocks__length'))['total_length'] or 0

    def recent_events(self, limit=5):
        return Event.objects.filter(
            clock_changes__clock__project__factions=self
        ).distinct().order_by('-when')[:limit]

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    timeline = models.ForeignKey(Timeline, related_name='projects', on_delete=models.CASCADE)
    factions = models.ManyToManyField(Faction, related_name='projects')
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def progress_percentage(self):
        """Calculate the project’s progress as a percentage based on all associated clocks."""
        total_length = self.clocks.aggregate(total_length=Sum('length'))['total_length'] or 1
        total_progress = sum(clock.calculate_progress() for clock in self.clocks.all())
        return (total_progress / total_length) * 100

    def is_finished(self):
        """Check if all clocks in the project are finished."""
        return all(clock.is_finished() for clock in self.clocks.all())

    def __str__(self):
        return f"{self.name} ({self.progress_percentage():.2f}%)"

class Clock(models.Model):
    title = models.CharField(max_length=100, blank=True)
    length = models.PositiveIntegerField()
    finished = models.IntegerField(default=0)
    project = models.ForeignKey(Project, related_name='clocks', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def calculate_progress(self):
        """Calculate the current progress of the clock by summing related ClockChange amounts."""
        return self.changes.aggregate(total_progress=Sum('amount'))['total_progress'] or 0

    def check_if_finished(self):
        """Mark the clock as finished if progress meets or exceeds its length."""
        if self.calculate_progress() >= self.length and self.finished == 0:
            latest_event = self.changes.order_by('-event__when').first()
            self.finished = latest_event.event.when if latest_event else 1
            self.save()

    def is_finished(self):
        """Check if the clock is finished."""
        return self.finished > 0

    def __str__(self):
        return f"{self.title or self.project.name} ({self.calculate_progress()}/{self.length})"

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    when = models.IntegerField()
    timeline = models.ForeignKey(Timeline, related_name='events', on_delete=models.CASCADE)
    # Changes stored as JSON: {'faction_id': amount, 'project_id': amount, 'clock_id': amount}
    changes = models.JSONField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} (When: {self.when})"

class ClockChange(models.Model):
    clock = models.ForeignKey('Clock', related_name='changes', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', related_name='clock_changes', on_delete=models.CASCADE)
    amount = models.IntegerField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Change of {self.amount} to {self.clock.title}"
