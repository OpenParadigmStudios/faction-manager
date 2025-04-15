# Getting Started with Faction Manager

This guide will walk you through the basic steps to get started with Faction Manager.

## Installation

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

6. Access the application at http://127.0.0.1:8000/

## Quick Start with Sample Data

For a quick start with sample data:

1. Navigate to http://127.0.0.1:8000/import-test-data/
2. The system will import pre-configured sample data

## Creating Your First Game

1. From the home page, click "Create New Game"
2. Fill in the name and description for your game
3. Click "Save" to create the game

## Adding Factions

1. From your game's detail page, click "Add Faction"
2. Fill in the faction details:
   - Name: The faction's name
   - Description: A brief overview
   - Tier: A numerical power rating (typically 1-5)
   - Goals, Leadership, Values, History: Additional details
3. Click "Save" to create the faction

## Creating Projects

1. From a faction's detail page, click "Add New Project"
2. Fill in the project details:
   - Name: The project's name
   - Description: What the project entails
   - Factions: Select which factions are involved
   - Length: How much progress is needed to complete (2-20)
3. Click "Save" to create the project

## Recording Events

1. From your game's detail page, click "Add Event"
2. Fill in the event details:
   - Name: A name for the event
   - Description: What happened
   - When: The time (in your game's timeline) when this occurred
3. Click "Save" to create the event

## Updating Project Progress

1. After creating an event, navigate to the project detail page
2. You'll see the event listed under "Events Affecting This Project"
3. Click on the event to add a ProjectChange record
4. Specify how much progress was made during this event

## Tracking Time

1. Create Sessions to mark your actual gameplay sessions
2. The "when" value of your latest session determines the current time in your game
3. Use this to track the passage of time and schedule future events

## Next Steps

Once you're comfortable with the basics:

- Explore the faction list to see all factions in your game
- Use the project list to track all ongoing projects
- Check event and session lists to view your game's timeline
- Consider adding more detailed faction information as your game progresses 