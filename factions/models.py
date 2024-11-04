from django.db import models
from django.db.models import Max

class Timeline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def now(self):
        now_value = self.sessions.aggregate(Max('when'))['when__max']
        return now_value if now_value is not None else 0
    
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
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    factions = models.ManyToManyField(Faction, related_name='projects')
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def active_clocks(self):
        return self.clocks.filter(finished__isnull=True)
    
    def completed_clocks(self):
        return self.clocks.filter(finished__isnull=False)
    
    def overall_progress(self):
        total_length = sum(clock.length for clock in self.clocks.all())
        if total_length == 0:
            return 0  # Avoid division by zero
        weighted_progress = sum(clock.progress() for clock in self.clocks.all())
        return min(weighted_progress / total_length * 100, 100)

    def __str__(self):
        return f"{self.name} ({self.overall_progress():.0f}%)"

class Clock(models.Model):
    title = models.CharField(max_length=100, blank=True)
    length = models.PositiveIntegerField()
    finished = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='clocks', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def progress(self):
        progress = sum(change['amount'] for change in self.clock_changes.all().values('amount'))
        return progress
    
    def is_finished(self):
        return self.progress() >= self.length
    
    def __str__(self):
        progress = min(self.progress() / self.length * 100, 100)  # Cap at 100%
        return f"{self.title if self.title else self.project.name} ({progress:.0f}%)"

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
    clock = models.ForeignKey(Clock, related_name='clock_changes', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='clock_changes', on_delete=models.CASCADE)
    amount = models.IntegerField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
