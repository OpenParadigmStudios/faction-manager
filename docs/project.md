# Project

Projects represent endeavors undertaken by factions. They have a clock/progress tracking system.

## Attributes

- **name**: The name of the project
- **description**: A detailed description of the project
- **game**: Reference to the Game this project belongs to
- **factions**: Many-to-many relationship with Factions working on this project
- **length**: The total amount of progress needed to complete the project
- **finished**: When the project was completed (NULL if not finished)
- **created_at**: Timestamp when the project was created
- **updated_at**: Timestamp when the project was last updated

## Functions

- **progress_percentage()**: Calculates the project's completion percentage
- **calculate_progress()**: Returns the current progress amount
- **check_if_finished()**: Marks project as finished if progress meets length
- **is_finished()**: Returns whether the project is complete

## Usage

Projects are central to the faction management system. They represent actions or endeavors that factions undertake to achieve their goals. Projects use a "clock" system with a specific length that requires a certain amount of progress to complete.

Progress on projects happens through Events which create ProjectChange records. As progress accumulates to meet or exceed the project's length, it is automatically marked as finished.

Projects can be associated with multiple factions, allowing for collaborative efforts.

### Views

- **ProjectListView**: Lists all projects in a specific game
- **ProjectDetailView**: Shows detailed information about a specific project
- **ProjectCreateView**: Allows creation of a new project
- **ProjectUpdateView**: Allows editing of an existing project
- **ProjectDeleteView**: Allows deletion of a project 