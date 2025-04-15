# Gameplay Examples

This document provides real-world examples of how Faction Manager can be used in actual play. Each example is drawn from typical tabletop roleplaying game scenarios to illustrate how the system helps GMs manage faction activities and developments.

## Example 1: Urban Intrigue Campaign

### Campaign Setup

**Game**: City of Shadows
**Time Units**: Each "when" unit represents one week of game time

**Initial Factions**:
- **The Nightwatch Guild** (Tier 3): Thieves guild controlling criminal activity
- **House Blackwood** (Tier 4): Noble family with political aspirations
- **The Veiled Hand** (Tier 2): Cult seeking magical artifacts
- **City Watch** (Tier 3): Law enforcement with corruption problems

**Initial Projects**:
- Nightwatch Guild: "Expand Territory into East District" (Length: 8)
- House Blackwood: "Discredit Rival Noble House" (Length: 6)
- The Veiled Hand: "Find the Orb of Shadows" (Length: 10)
- City Watch: "Clean Up Corruption" (Length: 12)

### Session Timeline

**Session 1** (When: 1):
- Players meet in a tavern and stop a robbery by Nightwatch Guild members
- They learn of political tensions between noble houses

**Post-Session Updates**:
1. Create Session record (When: 1)
2. Create Event: "Failed Robbery at Silver Tankard" (When: 1)
   - Add ProjectChange: -1 progress to "Expand Territory" for Nightwatch Guild
3. Create Event: "House Blackwood Spreads Rumors" (When: 1)
   - Add ProjectChange: +2 progress to "Discredit Rival Noble House"

**Session 2** (When: 3):
- Two weeks pass in game time
- Players investigate cult activity and discover a Veiled Hand ritual
- They interrupt the ritual but some cultists escape with a clue to the Orb's location

**Post-Session Updates**:
1. Create Session record (When: 3)
2. Create Event: "Interrupted Ritual" (When: 3)
   - Add ProjectChange: +1 progress to "Find the Orb of Shadows"
3. Create Event: "Nightwatch Bribes Officials" (When: 2)
   - Add ProjectChange: +2 progress to "Expand Territory"
4. Create Event: "Watch Captain Fired for Corruption" (When: 3)
   - Add ProjectChange: +3 progress to "Clean Up Corruption"

**Review and Planning**:
- House Blackwood's project is now at 2/6 progress
- Nightwatch Guild's project is at 1/8 progress (2 steps forward, 1 step back)
- Veiled Hand's project is at 1/10 progress
- City Watch's project is at 3/12 progress

## Example 2: Fantasy Kingdom Campaign

### Campaign Setup

**Game**: The Fractured Realm
**Time Units**: Each "when" unit represents one month

**Initial Factions**:
- **The Crown** (Tier 5): Royal family and their direct servants
- **Circle of Mages** (Tier 3): Magic users' guild with significant influence
- **The Old Faith** (Tier 4): Traditional religious organization
- **Border Raiders** (Tier 2): Organized bandits causing trouble

**Initial Projects**:
- The Crown: "Build New Royal Road" (Length: 15)
- Circle of Mages: "Research Ancient Magic" (Length: 8)
- The Old Faith: "Expand Temple Network" (Length: 10)
- Border Raiders: "Establish Wilderness Stronghold" (Length: 6)

### Session Timeline

**Session 1** (When: 1):
- Players are hired as caravan guards on a dangerous route
- They fight off Border Raiders and discover plans for their stronghold

**Post-Session Updates**:
1. Create Session record (When: 1)
2. Create Event: "Caravan Raid Foiled" (When: 1)
   - Add ProjectChange: -2 progress to "Establish Wilderness Stronghold"

**Between Sessions**:
1. Create Event: "Road Construction Begins" (When: 1)
   - Add ProjectChange: +3 progress to "Build New Royal Road"
2. Create Event: "Old Faith Missionaries Sent Out" (When: 1)
   - Add ProjectChange: +2 progress to "Expand Temple Network"
3. Create Event: "Mage Research Breakthrough" (When: 1)
   - Add ProjectChange: +3 progress to "Research Ancient Magic"

**Session 2** (When: 3):
- Two months pass in game time
- Players visit the capital and learn of tensions between the Crown and Mages
- They discover that the Ancient Magic being researched might be dangerous

**Post-Session Updates**:
1. Create Session record (When: 3)
2. Create Event: "Crown Restricts Magic Research" (When: 3)
   - Add ProjectChange: -1 progress to "Research Ancient Magic"
3. Create Event: "Border Raiders Regroup" (When: 2)
   - Add ProjectChange: +3 progress to "Establish Wilderness Stronghold"
4. Create Event: "Road Construction Continues" (When: 2-3)
   - Add ProjectChange: +4 progress to "Build New Royal Road"
5. Create Event: "Temple Construction Delayed by Weather" (When: 2-3)
   - Add ProjectChange: +1 progress to "Expand Temple Network"

**Project Completion Check**:
- Circle of Mages' "Research Ancient Magic" is now at 5/8
- Border Raiders' "Establish Wilderness Stronghold" is at 1/6
- The Crown's "Build New Royal Road" is at 7/15
- The Old Faith's "Expand Temple Network" is at 3/10

## Example 3: Science Fiction Colony Campaign

### Campaign Setup

**Game**: New Horizon Colony
**Time Units**: Each "when" unit represents one colony month (35 Earth days)

**Initial Factions**:
- **Colonial Administration** (Tier 4): Official government body
- **Corporate Interests** (Tier 4): Profit-focused business consortium
- **Scientists' Coalition** (Tier 2): Research-focused academics
- **Freedom Collective** (Tier 1): Anti-corporate activists

**Initial Projects**:
- Colonial Administration: "Secure the Perimeter" (Length: 8)
- Corporate Interests: "Establish Mining Operation" (Length: 10)
- Scientists' Coalition: "Study Indigenous Lifeforms" (Length: 6)
- Freedom Collective: "Build Underground Network" (Length: 4)

### Campaign Progress

**Session 1** (When: 1):
- Players arrive as new colonists and witness tension between corporations and scientists
- They help resolve a security issue at the perimeter

**Post-Session Updates**:
1. Create Session record (When: 1)
2. Create Event: "Perimeter Breach Contained" (When: 1)
   - Add ProjectChange: +2 progress to "Secure the Perimeter"
3. Create Event: "Corporate Survey Team Deployed" (When: 1)
   - Add ProjectChange: +2 progress to "Establish Mining Operation"

**Between Sessions**:
1. Create Event: "Scientists Collect Specimens" (When: 1)
   - Add ProjectChange: +1 progress to "Study Indigenous Lifeforms"
2. Create Event: "Freedom Collective Distributes Propaganda" (When: 1)
   - Add ProjectChange: +2 progress to "Build Underground Network"

**Session 2** (When: 3):
- Two colony months pass
- Players discover Corporate Interests are poisoning indigenous life
- They help Scientists' Coalition document the evidence

**Post-Session Updates**:
1. Create Session record (When: 3)
2. Create Event: "Corporate Pollution Exposed" (When: 3)
   - Add ProjectChange: -2 progress to "Establish Mining Operation"
   - Add ProjectChange: +3 progress to "Study Indigenous Lifeforms"
3. Create Event: "Freedom Collective Gains Supporters" (When: 3)
   - Add ProjectChange: +2 progress to "Build Underground Network"
4. Create Event: "Perimeter Expansion" (When: 2)
   - Add ProjectChange: +3 progress to "Secure the Perimeter"

**Project Completion Check**:
- Freedom Collective's "Build Underground Network" is now at 4/4 (COMPLETE)
- Create new project for Freedom Collective: "Sabotage Mining Operation" (Length: 8)

## Narrative Developments

These examples show how the system tracks the evolving narrative:

1. **Competing Interests**: In Example 3, as the Freedom Collective completes its network, they begin actively opposing Corporate Interests with a new project.

2. **Project Interactions**: In Example 2, the Crown's restriction of magic research directly impacts the Circle of Mages' project.

3. **Player Impact**: Players consistently influence project progress through their actions, sometimes helping (securing the perimeter) and sometimes hindering (exposing corporate pollution).

4. **World Evolution**: The system tracks how the world changes over time - the Border Raiders regroup after a setback, and the Freedom Collective grows from a small group to an organized resistance.

## Using These Examples

When running your own game:

1. After each session, create events for both what happened "on-screen" (with players) and "off-screen" (faction activities).

2. Use tier levels to determine how much progress factions make on their own. Higher tier factions generally make 1-3 points of progress per time unit on their projects.

3. When projects complete, consider what new projects might logically follow.

4. Use project progress to drive the narrative - if a project is nearly complete, it might become a focal point for the next session. 