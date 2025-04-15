# Development Guide

This guide is intended for developers who want to extend or modify the Faction Manager application.

## Architecture Overview

Faction Manager follows a standard Django Model-View-Template (MVT) architecture:

- **Models**: Defined in `factions/models.py`
- **Views**: Defined in `factions/views.py`
- **Templates**: Located in `factions/templates/`
- **URLs**: Defined in `factions/urls.py`
- **Forms**: Defined in `factions/forms.py`
- **Static Files**: Located in `factions/static/`

## Setting Up a Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/faction-manager.git
   cd faction-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
faction-manager/
├── factions/                 # Main application directory
│   ├── data/                # Data files for testing
│   ├── migrations/          # Database migrations
│   ├── static/              # Static files (CSS, JS)
│   ├── templates/           # HTML templates
│   ├── admin.py            # Admin interface configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   ├── utils.py            # Utility functions
│   └── views.py            # View logic
├── factionmanager/          # Project settings
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## Key Relationships

- **Game** is the top-level container for all other entities
- **Faction** belongs to a Game and can be associated with multiple Projects
- **Project** belongs to a Game, can be associated with multiple Factions
- **Event** belongs to a Game and is linked to Projects through ProjectChange
- **Session** belongs to a Game
- **ProjectChange** links Projects and Events, tracking progress changes

## Adding New Features

### Adding a New Model

1. Define the model in `factions/models.py`
2. Create and run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Register the model in `factions/admin.py` for admin interface
4. Create views in `factions/views.py`
5. Add URL patterns in `factions/urls.py`
6. Create templates in `factions/templates/`

### Extending Existing Models

1. Add new fields to the model in `factions/models.py`
2. Create and run migrations
3. Update relevant forms in `factions/forms.py`
4. Modify templates to display new fields

### Adding New Views

1. Create the view class or function in `factions/views.py`
2. Add a URL pattern in `factions/urls.py`
3. Create or update templates as needed

## Common Patterns

### Context Extension in Class-Based Views

```python
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['game'] = Game.objects.get(id=self.kwargs['game_id'])
    return context
```

### Filtering Querysets by Game

```python
def get_queryset(self):
    return Faction.objects.filter(game_id=self.kwargs['game_id'])
```

### Model Helper Methods

```python
def progress_percentage(self):
    total_length = self.length or 1
    total_progress = self.calculate_progress()
    return (total_progress / total_length) * 100
```

## Testing

Currently, the application does not have comprehensive tests. Consider adding tests using Django's testing framework:

1. Write model tests in `factions/tests.py`
2. Run tests with:
   ```bash
   python manage.py test
   ```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests if available
5. Submit a pull request 