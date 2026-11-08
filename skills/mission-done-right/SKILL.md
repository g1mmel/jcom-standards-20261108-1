---
name: mission-done-right
description: Build, fix or polish a campaign mission or campaign map in cnc_rev so a player can open it and enjoy it. Use for any work on data/missions, data/campaign, campaign maps, the campaign HUD or mission rendering.
---

# Mission done right

Owner, 2026-10-16: "get one done right and then approach the rest". A mission is done when a player opens it and it looks, reads and plays like a Command & Conquer mission.

## 1. See it the way the player sees it
- Take stills at 1600x900 with GPU flags on a private preview port.
- Open every still and describe what you see in your report.
- Put each still next to the reference view, `index.html?map=premade_kharg_gulf`: 3D relief, textured ground, water, trees, rocks, real buildings. Match or beat it.
- Check that the screen is clean: the briefing sits on its own, campaign mode shows only player panels, and player text is plain words a player needs.

## 2. Fix the cause
- When something looks wrong, find out why first. Trace it to the data or code that makes it, and fix it there.
- Keep the mission's map, the shared rules and the real numbers. Earn every pass.
- Known causes and fixes:
  - Big pad height deltas come from 0 m holes in the height data. Fill them from neighbours, then flatten the pad (status/map-kharg-shiraz-pads.md).
  - Flat render: see "Render faults" below.
- After 30 minutes on one cause, write what you checked to lanes/advice/<lane>-<n>.q.md and keep working on the next item while you wait.

## 3. The mission bar
1. **Looks like the game:** section 1.
2. **Reads like C&C:** an in-engine camera intro (no video, OR-012), a short briefing in plain STE English, an objective list, an EVA line for each objective, and win and loss end screens.
3. **Plays well:**
   - Teach one thing, then test it.
   - Enemy pressure comes from the map's real approaches. Waves are set in data and scale with easy, medium and hard.
   - One optional objective with a reward, and one mid-mission story beat.
   - A loss that can happen in normal play.
   - Length comes from the objectives.
4. **Measured:** the skirmish AI plays the player side, 3 seeds per difficulty. Each seed gives a different run. Report the win rate and time per difficulty.
5. **Campaign screen:** player panels only, and the tab title reads "JSLC and Conquer - <mission title>".
6. **Runs smoothly:** 60 fps at the default tier, with a clean console.

## 4. Report
Give a checklist against the bar. Mark each line met or not met, and link the still that shows it. Name every miss plainly; that is how the next lane learns.

## 5. Teach the next lane
When an advisor or your own digging teaches you something this skill does not say, add it here: short, general, with the file that proves it.

## Render faults
(Root causes and fixes are added here as they are found.)
