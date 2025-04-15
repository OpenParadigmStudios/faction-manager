# Event

Events represent significant occurrences in the game timeline that can affect projects.

## Attributes

- **name**: The name of the event
- **description**: A detailed description of the event
- **when**: The timestamp when this event occurs in game time
- **game**: Reference to the Game this event belongs to
- **created_at**: Timestamp when the event was created
- **updated_at**: Timestamp when the event was last updated

## Usage

Events represent important moments in your game's timeline. They serve both as narrative markers and as mechanisms to update project progress. Each event has a "when" attribute that places it in the game's timeline.

Events are connected to projects through ProjectChange records, which track how much progress was made on specific projects during the event.

### Views

- **EventListView**: Lists all events in a specific game
- **EventDetailView**: Shows detailed information about a specific event
- **EventCreateView**: Allows creation of a new event

## Example

An event might be "The Night of Broken Glass" where a faction's headquarters is raided. This event could result in negative progress on some of their projects but might accelerate progress on a "Revenge" project. 