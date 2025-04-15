# ProjectChange

ProjectChanges track how projects evolve during events.

## Attributes

- **project**: Reference to the Project being modified
- **event**: Reference to the Event during which the change occurs
- **amount**: The amount of progress added or subtracted
- **created_at**: Timestamp when the change was created
- **updated_at**: Timestamp when the change was last updated

## Usage

ProjectChanges are the mechanism through which project progress is updated. When significant events occur in your game world, you can create ProjectChange records to reflect how these events affected various projects.

The amount attribute can be positive (representing progress) or negative (representing setbacks). The total progress of a project is the sum of all its related ProjectChange amounts.

ProjectChanges connect events to projects, allowing you to track not just how much progress has been made on a project, but when and why that progress occurred.

## Example

If a faction successfully completes a heist, you might create an Event "The Great Heist" and then create ProjectChange records for various projects:
- +2 progress on their "Acquire Funding" project
- -1 progress on their "Maintain Low Profile" project
- +1 progress on a rival faction's "Hunt Down Thieves" project 