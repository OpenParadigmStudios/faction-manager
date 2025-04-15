# Faction Manager

A Django-based web application for managing factions, projects, and events in tabletop role-playing games.

## Overview

Faction Manager is a web application designed to help game masters and players track the progress of factions, their projects, and related events in tabletop role-playing games. The application provides a structured way to manage game timelines, faction activities, and project progress.

## Features

- **Game Management**
  - Create and manage multiple games
  - Track game sessions and events
  - View game timelines and progress

- **Faction Management**
  - Create and manage factions with detailed information
  - Track faction goals, leadership, values, and history
  - Monitor faction tier levels

- **Project Management**
  - Create and track projects associated with factions
  - Set project lengths and track progress
  - Monitor project completion status

- **Event System**
  - Record events that affect projects
  - Track project changes over time
  - Maintain chronological order of events

## Documentation

Comprehensive documentation is available in the [docs](docs/) directory:

- [Getting Started Guide](docs/getting_started.md)
- [Development Guide](docs/development.md)

### Core Models
- [Game](docs/game.md)
- [Faction](docs/faction.md)
- [Project](docs/project.md)
- [Event](docs/event.md)
- [Session](docs/session.md)
- [ProjectChange](docs/project_change.md)

### Features
- [Timeline Tracking](docs/timeline_tracking.md)
- [Data Import System](docs/data_import.md)

## Technical Stack

- **Backend**: Django 5.1.2
- **Database**: SQLite (default)
- **Dependencies**:
  - asgiref==3.8.1
  - Django==5.1.2
  - sqlparse==0.5.1

## Project Structure

```
faction-manager/
├── docs/                   # Documentation directory
├── factions/                # Main application directory
│   ├── data/               # Data files for testing
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files
│   ├── templates/          # HTML templates
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Form definitions
│   ├── models.py          # Database models
│   ├── urls.py            # URL routing
│   ├── utils.py           # Utility functions
│   └── views.py           # View logic
├── factionmanager/         # Project settings
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd faction-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
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

## Quick Start

For a quick introduction to using Faction Manager:

1. Follow the [Installation](#installation) steps above
2. Access http://127.0.0.1:8000/import-test-data/ to load sample data
3. Navigate to http://127.0.0.1:8000/ to start using the application
4. See the [Getting Started Guide](docs/getting_started.md) for more details

## License

This project is licensed under the terms included in the LICENSE file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. See the [Development Guide](docs/development.md) for details on how to set up a development environment and contribute to the project.