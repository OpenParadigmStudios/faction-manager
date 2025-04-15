# Faction

Factions represent organizations, groups, or entities within a game that have goals and undertake projects.

## Attributes

- **name**: The name of the faction
- **description**: A detailed description of the faction
- **tier**: A numerical representation of the faction's power/influence
- **goals**: The faction's objectives
- **leadership**: Information about who leads the faction
- **values**: What the faction stands for
- **history**: Background information about the faction
- **game**: Reference to the Game this faction belongs to
- **created_at**: Timestamp when the faction was created
- **updated_at**: Timestamp when the faction was last updated

## Functions

- **active_projects()**: Returns all unfinished projects for this faction
- **completed_projects()**: Returns all finished projects for this faction
- **total_clock_length()**: Returns the combined length of all projects
- **recent_events(limit=5)**: Returns events that have affected this faction

## Usage

Factions are the main actors in your game world. They have goals and undertake projects to achieve them. 
Factions can be ranked by tiers to indicate their relative power in the game world.

### Views

- **FactionListView**: Lists all factions in a specific game
- **FactionDetailView**: Shows detailed information about a specific faction
- **FactionCreateView**: Allows creation of a new faction
- **FactionUpdateView**: Allows editing of an existing faction
- **FactionDeleteView**: Allows deletion of a faction 