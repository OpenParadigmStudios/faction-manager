# Session

Sessions represent gameplay sessions with their own timeline position.

## Attributes

- **name**: The name of the session
- **description**: A detailed description of the session
- **when**: The timestamp when this session occurs in game time
- **game**: Reference to the Game this session belongs to
- **created_at**: Timestamp when the session was created
- **updated_at**: Timestamp when the session was last updated

## Usage

Sessions represent actual play sessions in your tabletop RPG. Each session has a "when" attribute that places it in the game's timeline. The latest session's "when" value is used to determine the current time in the game world.

Sessions serve as a way to organize events and track the passage of time in your game world. They can contain notes about what happened during the gameplay session.

### Views

- **SessionListView**: Lists all sessions in a specific game
- **SessionDetailView**: Shows detailed information about a specific session
- **SessionCreateView**: Allows creation of a new session

## Example

After running a game session where players interact with several factions, you might create a Session record with name "Session 5: The Council Meeting" and description "Players attended the faction council and negotiated a treaty." The "when" value would represent when this occurred in the game world timeline. 