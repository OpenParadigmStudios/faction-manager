# Data Import System

Faction Manager supports importing test data from YAML files located in the data directory.

## Overview

The data import system allows you to quickly populate your Faction Manager instance with pre-defined data. This is particularly useful for testing, demonstrations, or starting a new game with a pre-built world.

## Supported Data Types

The system can import the following types of data:

- Games
- Factions
- Projects
- Events
- Sessions
- ProjectChanges

## Directory Structure

Data files should be placed in subdirectories under the `factions/data/` directory, with each entity type having its own subdirectory:

```
factions/data/
├── game/           # Game YAML files
├── faction/        # Faction YAML files
├── project/        # Project YAML files
├── event/          # Event YAML files
├── session/        # Session YAML files
└── projectchange/  # ProjectChange YAML files
```

## File Format

Data files use YAML format and can contain either a single entity or a list of entities:

### Single Entity Example

```yaml
name: Empire
game: Star Wars
description: The Galactic Empire rules with an iron fist
tier: 3
goals: Crush the Rebellion
leadership: Emperor Palpatine
values: Order, Control, Power
history: Rose from the Republic after the Clone Wars
```

### Multiple Entities Example

```yaml
- name: Empire
  game: Star Wars
  description: The Galactic Empire
  tier: 3
  
- name: Rebellion
  game: Star Wars
  description: The Rebel Alliance
  tier: 2
```

## Import Process

To import test data:

1. Place YAML files in the appropriate subdirectories
2. Navigate to `/import-test-data/` in your browser
3. The system will process all YAML files and create or update records accordingly

## Import Order

The import process follows a specific order to ensure that dependencies are satisfied:

1. Games (must exist before other entities)
2. Factions (reference Games)
3. Projects (reference Games and Factions)
4. Sessions (reference Games)
5. Events (reference Games)
6. ProjectChanges (reference Projects and Events)

## Usage Notes

- Existing entities with matching names will be updated rather than duplicated
- Many-to-many relationships (like between Projects and Factions) are properly maintained
- The import system handles references between entities using name lookups 