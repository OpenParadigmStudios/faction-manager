# Timeline Tracking

The system tracks a game timeline using the "when" field on Events and Sessions.

## Overview

Timeline tracking is a core feature of Faction Manager. It allows you to maintain a chronological record of events and sessions in your game world, making it easier to track narrative developments and faction activities.

## How It Works

- The current time in a game world is determined by the latest Session's "when" value
- Events are chronologically ordered by their "when" value
- Project progress is tracked over time through Events and their associated ProjectChanges

## Time Units

The "when" field is an integer value that can represent any time unit you prefer for your game:

- Game days (e.g., Day 1, Day 2, etc.)
- Game weeks or months
- Years in a custom calendar
- Abstract time periods

## Timeline Views

The application presents timeline information in several ways:

- Game details show the current time ("Now")
- Session and Event lists are ordered by their "when" value
- Project details show when progress was made through linked events

## Usage Examples

### Tracking Campaign Progress

If your game represents a long-running campaign, you might set "when" values to represent days or weeks in the game world. As the campaign progresses, the "Now" value advances, and you can see how factions and projects have evolved over time.

### Managing Downtime

Between game sessions, you can create events with appropriate "when" values to represent faction activities during downtime. This allows for dynamic world development even when players aren't directly involved. 