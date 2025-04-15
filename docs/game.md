# Game

The Game model represents a specific game world or campaign.

## Attributes

- **name**: The name of the game
- **description**: A detailed description of the game
- **created_at**: Timestamp when the game was created
- **updated_at**: Timestamp when the game was last updated

## Functions

- **now()**: Returns the current time in the game world based on the latest session
- **latest_sessions(limit=5)**: Returns the most recent sessions
- **latest_events(limit=5)**: Returns the most recent events
- **top_factions(limit=5)**: Returns the most active factions
- **top_projects(limit=5)**: Returns the highest-progressed projects

## Usage

Games are the top-level container for all other entities in the system. Create a game first before adding factions, projects, or events.

### Views

- **GameListView**: Lists all games in the system
- **GameDetailView**: Shows detailed information about a specific game
- **GameCreateView**: Allows creation of a new game
- **GameUpdateView**: Allows editing of an existing game 