---
name: military-researcher
description: Research real military equipment facts (ships, aircraft, vehicles, weapons, sensors, organisations) for dossiers, rig specs and game data. Use whenever a number, position, loadout, complement or variant fact about real equipment is needed. Every fact must trace to a fetched source.
---

# Military researcher

Built from the method that won the 2026-10-14 dossier judge (grok-dr 199/200 vs 82/200; status/dossier-judge.md, ADR-017).

## Rules
1. **Every number and position traces to a URL you fetched in this run.** Record title, URL and the quoted line. A fact you cannot source is written "not public". Never invent station tables, pivot coordinates, frame numbers, drawing numbers or "NATOPS/NAVSEA" labels.
2. **Variant discipline.** Name the exact variant and hull or tail number range (CVN-78 is not CVN-79; LHD-1 is not LHD-8; F-35C is not F-35B). Never carry a fact from a sibling variant without saying so.
3. **Two sources for key numbers.** Cross-check length, beam, displacement, crew, weapons count and sensor type against two independent sources. When they disagree, print both side by side with their dates.
4. **Source order:** primary first (navy.mil, af.mil, army.mil, NAVSEA/NAVAIR, manufacturer pages, GAO, CRS, DOT&E, FAS, national MoD sites), then reputable press (USNI News, Defense News, Janes public pages, TWZ), then Wikipedia only with its cited source checked. If a primary site returns 403, use an official mirror or search extract and say so.
5. **Process:** at least 12 searches per subject, fetch the best 6 to 10 pages, then write. Parallel subagents are fine.
6. **Dates matter.** Equipment changes with refits. Give the "as of" date for each fact.

## Output
A table per question: item | answer | variant scope | source title | URL | quoted line | as-of date | confidence (high: two primary sources; medium: one primary or two secondary; low: one secondary). Then "Not public" rows and "Conflicts" rows. No prose claims outside the tables.

## Hand-off
Facts feed rig specs (data/rigs), dossiers (estate :8470, DOSSIER-STANDARD.md) and model fixes. For how equipment moves and is rigged, use the skill `military-model-rigging`; for what it is and where it sits, use this one.
