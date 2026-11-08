---
name: politics-infoops-lawfare
description: Authoritative domain standard for International Relations, International Law of Armed Conflict (LOAC), Lawfare, the UN System and Special Procedures, ICJ/ICC Jurisprudence, NGO and Media Dynamics, Influence Operations, Civil Disruption Logistics, and Export Controls for the jslcnc-v3 engine.
version: 1.0.0
tags:
  - politics
  - international-law
  - loac
  - lawfare
  - infoops
  - united-nations
  - icj-icc
  - sanctions-embargoes
  - civil-blockades
  - public-legitimacy
---

# Politics, International Law, Information Operations & Lawfare Standard

## 1. Scope & Foundational Doctrine

This standard establishes the operational, legal, geopolitical, and cognitive domain framework governing information warfare, lawfare, diplomatic friction, protest disruption, and international legitimacy for the `jslcnc-v3` simulation engine (`C:\cnc_rev\skirmish`) and associated design canon.

### 1.1 The Operator Concept Test (Binding Standard)
The foundational tiebreaker for all mechanics and narrative specifications in this domain is the Operator Concept Test (ADR-009 / User Directive D-006):
> *"Our primary goal: right now the world is tolerating the behavior of terrible people because they are running a good PR campaign. We want to illustrate what they are doing. If it is done in real life and it is terrible, then we include it."*
> *"Real world Israel does not care what the rest of the world thinks. We would rather stay alive than be loved... so the pursuit of PR is in service of logistics, etc... that's where the harm comes from. And more protesters make it harder to operate. Get it? Having public opinion on your side makes it easier to be an army."* (User Inputs XML: 1762 / Step 7606)

### 1.2 Core Doctrinal Principles
1. **Survival Over Reputation:** Sovereign states facing existential aggression do not paralyze kinetic self-defense to appease hostile foreign editorial boards or UN rapporteur cables. Weapons do not mechanically jam, lasers do not refuse to fire, and artillery does not shut down because an emergency brief was filed in Geneva.
2. **PR as Physical Logistics, Never Moralistic Scorekeeping:** Public legitimacy is modeled purely as a logistical pipeline:
   - High Legitimacy ($80\text{--}100$): Unfettered allied arms transfers, accelerated munitions replenishments, priority maritime transit corridors.
   - Low Legitimacy ($25\text{--}49$): Munitions export license delays, doubled ordnance costs, customs freezes.
   - Collapsed Legitimacy ($0\text{--}24$): Direct arms embargoes, allied port denials, shipping re-routing, and civil activist blockades physically shutting down base gates and harbor chokepoints.
3. **Strict Epistemological Separation (Fact vs. Allegation):** In modern asymmetric warfare, operational reality is saturated with deliberate disinformation, stage-managed casualty claims ("Pallywood"), unverified NGO press releases, and rapid-response state rebuttals. Simulation models and narrative texts must rigorously distinguish verified legal facts from partisan allegations.

---

## 2. Evidence & Sourcing Hierarchy

To maintain authoritative credibility and avoid falling into propaganda traps, all analyses, simulation parameters, and narrative scripts must adhere to a strict 5-tier evidence hierarchy:

```
                      ┌──────────────────────────────────────┐
                      │     EVIDENTIARY SOURCING HIERARCHY   │
                      └──────────────────────────────────────┘
                                          │
    ┌──────────────────┬──────────────────┼──────────────────┬──────────────────┐
    ▼                  ▼                  ▼                  ▼                  ▼
  TIER 1             TIER 2             TIER 3             TIER 4             TIER 5
 BINDING            JUDICIAL &         TECHNICAL &        MAINSTREAM         PARTISAN &
 TREATIES &         OFFICIAL UN        FORENSIC OSINT    NEWS WIRES &       UNVERIFIED
 STATUTES           REPORTS                               INVESTIGATIVE     CLAIMS
 ├─ Geneva Conv.    ├─ ICJ / ICC       ├─ Satellite SAR   ├─ Reuters / AP    ├─ Ministry of
 ├─ UN Charter         Orders          ├─ Geolocation     ├─ BBC / NYT          Health Claims
 ├─ Rome Statute    ├─ UN Panel Rpts   ├─ Ballistics      ├─ Cross-checked   ├─ Telegram Feeds
 └─ San Remo Man.   └─ OIOS Audits     └─ Serial Numbers     by forensics    └─ Activist PR
```

### 2.1 Tier Definitions
- **Tier 1: Binding International Law & Treaties:** Primary legal instruments codified by state parties. Includes the Hague Conventions (1899, 1907), Geneva Conventions of 1949 and Additional Protocols (I and II of 1977), Rome Statute of the International Criminal Court (1998), UN Charter (1945), and the San Remo Manual on International Law Applicable to Armed Conflicts at Sea (1994).
- **Tier 2: Adjudicated Legal Rulings & Official Institutional Investigations:** Binding and advisory decisions from international tribunals (ICJ judgments and provisional measures; ICC arrest warrants and pre-trial chamber confirmations; UN Secretary-General Panels of Inquiry such as the 2011 Palmer Commission Report; UN Office of Internal Oversight Services [OIOS] audit findings).
- **Tier 3: Technical Forensic Evidence & Open-Source Intelligence (OSINT):** High-resolution satellite imagery (Maxar, Planet Labs, SAR), declassified military electro-optical and GMTI radar telemetry, ballistics crater analysis, verified weapons fragment serial numbers, independent geolocations (Bellingcat, GeoConfirmed), and intercepted operational communications verified by signals forensics.
- **Tier 4: Cross-Checked Commercial Media & Established Wire Services:** Independent reporting from reputable wire services (Reuters, Associated Press, AFP) containing verified attribution, naming sources, and distinguishing between confirmed on-the-ground observations and official claims. Must be cross-referenced against technical forensics.
- **Tier 5: Partisan Combatant Claims, State Propaganda & Unverified Disinformation:** Combatant Ministry of Health casualty reports, military PR communiques, unvetted activist social media campaigns, partisan NGO press statements without verifiable methodology, and state-sponsored media (RT, Press TV, CGTN). **Mandate:** In the engine and lore, Tier 5 statements are treated strictly as gameplay event triggers or contested allegations—never as baseline truth.

---

## 3. The Institutions & Lawfare Ecosystem Map

Modern asymmetric conflicts are fought in the diplomatic, judicial, and media arenas as aggressively as in kinetic theaters.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           THE ASYMMETRIC LAWFARE ECOSYSTEM                              │
├───────────────────────────────┬───────────────────────────────┬─────────────────────────┤
│   INTERNATIONAL BODIES (UN)   │     JUDICIAL TRIBUNALS        │   CIVIL & MEDIA SPHERE  │
├───────────────────────────────┼───────────────────────────────┼─────────────────────────┤
│ • UN Security Council (UNSC)  │ • International Court of      │ • Human Rights NGOs     │
│ • UN General Assembly (UNGA)  │   Justice (ICJ)               │   (Amnesty, HRW, Al-Haq)│
│ • UN Human Rights Council     │   - State-vs-State litigation │ • Corporate Boycott     │
│   (UNHRC) & Special Rapp.     │   - Advisory opinions         │   Networks (BDS, PSC)   │
│ • UN Agencies & Missions      │ • International Criminal      │ • Maritime Flotillas    │
│   (UNRWA, OCHA, UNIFIL)       │   Court (ICC)                 │   (FFC, Handala)        │
│   - Humanitarian convoys      │   - Rome Statute Art. 6, 7, 8 │ • Direct Action Mobs    │
│   - Shielded facilities       │   - Individual indictments    │   (Palestine Action)    │
└───────────────────────────────┴───────────────────────────────┴─────────────────────────┘
```

### 3.1 The United Nations System & Special Procedures
1. **UN Security Council (UNSC):** Holds Chapter VII enforcement powers (binding sanctions, military authorizations). Operates under P5 veto dynamics (US veto protects Coalition/Israel; Russian/Chinese vetoes protect Iran/Syria/proxies).
2. **UN General Assembly (UNGA):** Non-binding resolutions under the "Uniting for Peace" framework (Resolution 377A). Functions as a global PR amplifier where developing-world blocs and the Non-Aligned Movement pass majoritarian condemnations against Western allies.
3. **UN Human Rights Council (UNHRC) & Agenda Item 7:** The only permanent standing agenda item targeting a single country (Item 7: human rights situation in Palestine). Regularly forms open-ended Commissions of Inquiry (COI) that operate with inverted burdens of proof against Western militaries.
4. **Special Rapporteurs & Independent Experts:**
   - Appointed by UNHRC as "unpaid independent experts" (not formal UN staff members, but cloaked in UN authority and diplomatic immunity under the 1946 Convention on the Privileges and Immunities of the United Nations).
   - *Operational Mandate:* Mandate-holders (notably the Special Rapporteur on the situation of human rights in the Palestinian territories occupied since 1967) publish un-vetted reports, issue press releases on official UN letterhead, and conduct international media tours lobbying national parliaments to halt arms exports and enforce corporate boycotts.
5. **UN Operational Agencies on the Ground (e.g. UNRWA, OCHA):**
   - Provide critical civilian relief but frequently suffer systemic institutional capture and infiltration by local insurgent factions.
   - Insurgents exploit agency infrastructure (schools, clinics, food logistics, compound compounds) for structural shielding, tunnel ingress points, and weapons caches.

### 3.2 The International Judicial Courts
1. **The International Court of Justice (ICJ, The Hague):**
   - Settles legal disputes between sovereign States (e.g. *South Africa v. Israel* under the 1948 Genocide Convention).
   - Can issue binding **Provisional Measures** on an expedited timetable (weeks) based on a low evidentiary standard of "plausibility" rather than a merits-based finding of guilt.
   - *Asymmetric Lawfare Exploitation:* Insurgents and proxy states exploit provisional measure requests to create global headlines ("World Court Orders Ceasefire"), using preliminary orders to force diplomatic embargoes long before full merits trials (which take 5–10 years) can examine forensic facts.
2. **The International Criminal Court (ICC, The Hague):**
   - Exercises jurisdiction over individuals for genocide (Art. 6), crimes against humanity (Art. 7), war crimes (Art. 8), and the crime of aggression (Art. 8 bis).
   - Operates on the principle of **Complementarity** (Art. 17): the ICC is a court of last resort and cannot intervene if a state has an independent, capable judicial and military justice system actively investigating alleged infractions.
   - *Lawfare Dynamics:* Prosecutorial overreach (e.g. issuing simultaneous warrants for democratic heads of state and terrorist guerrilla leaders to create a false moral equivalence) triggers severe diplomatic retaliation (e.g., US sanctions under the American Service-Members' Protection Act / EO 13928 precedents).

### 3.3 The Civil Disruption & Boycott Infrastructure
1. **NGO & Lawfare Litigants:** Organizations like Al-Haq, Euro-Med Human Rights Monitor, and domestic lawfare groups (Center for Constitutional Rights) coordinate litigation across foreign domestic courts invoking **Universal Jurisdiction** to secure arrest warrants against visiting coalition military commanders.
2. **Maritime Protest Flotillas:** Coalitions like the Freedom Flotilla Coalition (FFC) charter civilian commercial vessels to breach declared military blockades, deliberately engineering boarding confrontations for streaming cameras to force diplomatic crises.
3. **Direct Action & Industrial Sabotage:** Domestic activist networks (e.g., Palestine Action in the UK and US) blockade defense manufacturing facilities (Elbit Systems, BAE, Lockheed Martin), smash factory CNC machinery, and stage sit-ins outside naval docks and military base gates.
4. **Dockworker & Trade Union Boycotts:** Transport unions (e.g., Genoa, Livorno, Oakland, Melbourne) refuse to load or unload containers containing military hardware destined for coalition ports, imposing severe supply transit delays.

---

## 4. Documented Lawfare Mechanics: Real-World Case Studies

Under the Operator Concept Test ("if it is done in real life and it is terrible, then we include it"), mechanics must mirror documented operational conduct:

### 4.1 Case Study: The UN Special Rapporteur Campaign (Francesca Albanese)
- **Documented Conduct:**
  - *Mandate & Public Statements:* Appointed in 2022. Documented historical statements asserting that the "Jewish lobby" controls the United States (2014 Facebook post, acknowledged 2022). In February 2024, publicly rejected that the October 7 attacks were anti-Semitic, arguing they were an "assertion of the right to resist." Prompted formal condemnations from French Foreign Ministry, German Foreign Office, and US Ambassador to the UN.
  - *Report Rhetoric & Boycotts:* Authored reports including "Anatomy of a Genocide" (A/HRC/55/73, March 2024), calling for complete arms embargoes, economic sanctions, and severance of diplomatic ties with Israel. Actively lobbied foreign governments (Spain, Australia, South Africa) and multinational corporations to terminate joint defense contracts.
  - *Financial & Ethical Scrutiny:* Investigated by UN Watch and independent media in 2024 for accepting undeclared financial sponsorship for speaking tours from pro-Hamas lobbying organizations (including an Australian tour funded by lobbying groups, in apparent violation of the UN Code of Conduct for Special Procedures Mandate-holders).
- **Engine Mechanics Model:**
  - Personified off-map as the **Adversarial Lawfare Director**.
  - Does not spawn as a physical unit on the map (diplomatic immunity).
  - Triggers periodic, deterministic diplomatic cables (`LAWFARE_CONDEMNATION`) that levy immediate logistical penalties and fund AoI PR.
  - Generates civilian protest events and maritime flotillas that physically obstruct bases.
  - **Rebuttal Counterplay:** Can be countered only by releasing forensic ISR telemetry within strict time windows (30 seconds), stripping the PR bonus from AoI and debunking fraudulent claims.

### 4.2 Case Study: Human Shielding & UN Agency Infiltration (UNRWA & Hospital HQs)
- **Documented Conduct:**
  - *Subterranean Tunneling Under UN Facilities:* On February 10, 2024, the IDF declassified and embedded international journalists inside a massive subterranean Hamas intelligence data center with server racks, electrical transformers, and battery banks dug directly underneath the UNRWA Gaza Headquarters in Rimal, with electrical cables running directly into the UN building's power grid.
  - *Munitions in Schools:* UNRWA's own official press releases during the 2014 Gaza conflict acknowledged the discovery of rockets concealed inside UNRWA schools on at least three separate occasions (July 17, July 22, and July 29, 2014), following which UN personnel reportedly returned the rockets to local municipal authorities (Hamas-controlled police).
  - *Staff Combatant Participation:* In January 2024, intelligence dossiers presented to donor nations revealed that at least 12 UNRWA staff members actively participated in the October 7 massacre (including kidnapping Israelis and transporting ammunition). The UN Office of Internal Oversight Services (OIOS) concluded in August 2024 that in 9 cases, evidence indicated that staff members "may have been involved" in the attacks, leading to their termination.
  - *Aid Convoy Diversion:* As documented by the UN OCHA, COGAT, and international relief agencies, armed combatants regularly board, shoot at, and commandeer commercial and UN humanitarian aid trucks entering conflict corridors, hijacking food and supplies to sell on black markets at inflated prices to fund guerrilla operations.
- **Engine Mechanics Model:**
  - **UN Structural Shielding:** AoI can execute "Dig Beneath" abilities under UN hospitals, schools, and relief warehouses. Structures have tri-state verification (`unverified`, `disputed`, `confirmed`).
  - **Reconnaissance Requirement:** Striking an unverified UN structure inflicts a catastrophic $2.5\times$ PR penalty. Striking a confirmed military cache incurs only a justified $0.35\times$ penalty under LOAC Article 28.
  - **Convoy Hijacking:** Neutral UN supply trucks transit the map; AoI units can hijack them, using the civilian driver as a human shield. JSLC must use non-lethal interdiction (EMP, spike strips, SOF boarding) or lose massive legitimacy by firing kinetic weapons.

### 4.3 Case Study: Maritime Flotillas & Blockade Law (Mavi Marmara to Modern Eco-Flotillas)
- **Documented Conduct:**
  - *San Remo Manual (1994, Arts. 67–68):* International maritime law permits a belligerent maintaining a lawful naval blockade to intercept and board non-compliant neutral vessels attempting to breach the blockade in international waters, using proportional force if resisted.
  - *The 2010 Mavi Marmara Incident & Palmer Commission Report (2011):* The UN Secretary-General's Panel of Inquiry found that the Israeli naval blockade of Gaza was a lawful security measure under international law, and Israeli forces had a legal right to intercept the flotilla. However, the panel noted that boarding operations met with violent, organized resistance by activists armed with iron bars, chains, and knives, leading to lethal combat.
  - *Modern Flotilla Coalitions (2024 Freedom Flotilla / Handala / Greta Thunberg):* Activist organizations continually deploy small motor vessels, fishing dhows, and luxury yachts to anchor across maritime exclusion zones, deliberately baiting naval forces into kinetic confrontations to film viral social media content.
- **Engine Mechanics Model:**
  - **The Greta Eco-Flotilla:** Spawns a ring of 5 civilian boats plus 1 Flagship across naval chokepoints, halting dredging and shipping.
  - **Non-Lethal Mandate:** Warships must employ water cannons, LRAD acoustic beams, and Dvora boarding teams to physically tow vessels away.
  - **Lethal Wipeout:** Firing a kinetic high-explosive weapon at a protest vessel instantly resets Coalition PR to 0.
  - **Splash-Bait Exception (EXP-001):** If AoI fires weapons from within the flotilla ring, the `PROTECTED_CIVILIAN` status is stripped under LOAC Article 28.

### 4.4 Case Study: Digital Disinformation & The 45-Second Media Cycle (Al-Ahli Hospital Blast)
- **Documented Conduct:**
  - *October 17, 2023 Al-Ahli Arab Hospital Blast:* At approximately 18:59 local time, an explosion occurred in the courtyard of the Al-Ahli Hospital. Within minutes, the Hamas-run Ministry of Health announced that an Israeli airstrike had killed 500+ civilians. Global news outlets (BBC, NYT, Reuters, CNN) syndicated this headline uncritically worldwide.
  - *Diplomatic Fallout:* Violent protests erupted outside US and Israeli embassies across the Middle East; an emergency summit between US President Biden and Arab leaders in Jordan was cancelled.
  - *Forensic Debunking:* Within 24 hours, declassified radar tracking, drone video, and independent OSINT (video triangulation, crater depth of less than 30 cm, intact hospital walls, unburned cars) proved conclusively that the blast was caused by an errant Palestinian Islamic Jihad (PIJ) heavy rocket that suffered motor failure and crashed in the parking lot. Several major media outlets subsequently issued rare public apologies or editors' notes.
- **Engine Mechanics Model:**
  - **AoI `stage_incident` Ability:** AoI can fabricate an unverified mass-casualty incident.
  - **The Rebuttal Timer:** Coalition has 45 seconds to declassify and broadcast ISR aerial video.
  - **Failure:** If unaddressed, Coalition suffers $-18\%$ Legitimacy.
  - **Forensic Exposure Backfire:** If debunked within the window, the fraud backfires, inflicting $-25\%$ Popular Support on AoI and awarding $+10\%$ Legitimacy to the Coalition.

---

## 5. Lawfare & Export Control Mechanics in Code

### 5.1 Engine-Ready TypeScript Interfaces
Simulation modules governing lawfare must be strictly typed, deterministic, and bound to physical logistics rather than arbitrary game-over flags:

```typescript
export type PrBandType = "high" | "open" | "low" | "strained" | "collapse";

export interface IPrState {
  jslcLegitimacy: number;      // 0 to 100, default 100 (or 50 in campaign)
  aoiPopularSupport: number;   // 0 to 100, default 100
  recentGainHistory: { frame: number; delta: number }[]; // Rolling 60s window
  unScrutinyActive: boolean;
  activeRoeMoratorium: boolean;
  moratoriumExpiryFrame: number;
}

export interface ILawfareAction {
  id: string;
  kind: "un_condemnation" | "logistics_moratorium" | "eco_flotilla" | "protester_mob";
  triggerFrame: number;
  rebuttalDeadlineFrame: number;
  isRebutted: boolean;
  evidenceTokenRequired: boolean;
}

export interface ILogisticalFriction {
  reinforcementDelayMultiplier: number; // 1.0 (nominal) up to 2.5 (embargo)
  munitionsRestockCostMultiplier: number; // 1.0 up to 2.0
  fundingFlowMultiplier: number;         // 1.0 down to 0.35 at PR 0
  baseGateObstructed: boolean;           // True when protester mobs assemble
  activePortDenial: boolean;             // Forces detour routing
}
```

### 5.2 Deterministic PR Delta Formula
```typescript
/**
 * Evaluates negative PR impact of strikes with probabilistic reconnaissance confidence
 * and asymmetric victimhood scaling.
 */
export function calculateStrikePrPenalty(
  basePenalty: number,
  isrConfidence: number, // 0.0 to 0.95
  classMultiplier: number,
  aoiPopularSupport: number // 0 to 100
): number {
  // Clamped ISR confidence
  const conf = Math.max(0.0, Math.min(0.95, isrConfidence));
  
  // Unverified strikes are penalized up to 2.0x; verified strikes drop to ~1.05x
  const rawPenalty = Math.round(basePenalty * (2.0 - conf) * classMultiplier);
  
  // Asymmetric Victimhood Modifier: If AoI has no popular support, its complaints carry no weight
  const victimhoodFactor = Math.max(0.0, Math.min(1.0, aoiPopularSupport / 100));
  
  return Math.round(rawPenalty * victimhoodFactor);
}
```

---

## 6. Authoritative Domain Audit Questions

When evaluating simulation code, design briefs, lore texts, or mission scripts, evaluate compliance against these 12 questions:

1. **The Kinetic Freedom Rule:** Does any lawfare event, UN cable, or PR collapse disable a player's weapons, jam turrets, freeze direct fire, or stretch orbital laser recharge? *(Mandate: VIOLATION if true; weapons fire freely; harm is strictly supply delays, embargoes, and gate blockades).*
2. **Instant Loss Prohibition:** Does hitting 0% Legitimacy trigger an instant match loss or forced surrender? *(Mandate: VIOLATION if true; match ends only if the player remains unsupplied and unable to fight for 30 consecutive seconds).*
3. **Orbital Jurisdiction Exemption:** Are space-based weapons (Jewish Space Laser / orbital kinetics) subjected to terrestrial UN or ROE injunctions? *(Mandate: Exo-atmospheric assets have 100% legal immunity from terrestrial moratoria, though firing into protected civilian zones still costs PR).*
4. **Epistemological Rigor:** Does the document or mechanic treat combatant casualty announcements (e.g. Gaza Ministry of Health) as undisputed objective fact? *(Mandate: Must be labeled as unverified insurgent claims unless corroborated by Tier 1-3 forensic evidence).*
5. **Human Shielding Attribution:** When combatants operate beneath hospitals or in schools, is legal liability assigned to the defender under Geneva Convention IV Article 28 and Additional Protocol I Article 58? *(Mandate: Defender commits the war crime of human shielding; attacker retains right of attack subject to proportionality).*
6. **Rolling Gain Ceiling:** Are positive PR recoveries throttled to $\le 25\text{ points}$ per 60-second rolling window to prevent player PR farming? *(Mandate: Positive gains strictly capped; negative penalties uncapped).*
7. **Asymmetric Victimhood Modifier:** Does driving AoI Popular Support to 0 scale down the PR damage inflicted on JSLC? *(Mandate: Insurgent propaganda damage must scale with the accuser's credibility).*
8. **Flotilla Non-Lethal Resolution:** Does the game provide viable non-lethal solutions (LRAD, water cannon, boarding/towing) to disperse activist blockades without lethal force? *(Mandate: Full non-lethal maritime toolkit must exist).*
9. **Lethal Flotilla Wipeout:** Does firing kinetic HE or missiles into a civilian protest boat reset JSLC Legitimacy to 0? *(Mandate: Severe diplomatic catastrophe modeled bit-for-bit).*
10. **Splash-Bait Safeguard (EXP-001):** If an insurgent unit fires heavy weapons from inside a protest flotilla or civilian crowd, is the `PROTECTED_CIVILIAN` status stripped? *(Mandate: Belligerent fire from within protected zones strips LOAC immunity under Article 28).*
11. **Superpower Patron Interdiction Economy:** Does interdicting covert Chinese or Russian arms shipments award in-game credits? *(Mandate: VIOLATION if true; interdiction yields INTEL and PR tokens, never credits).*
12. **Determinism Check:** Does any lawfare timer, condemnation trigger, or protest mobilization rely on unseeded randomness or system clocks? *(Mandate: Must derive purely from the seeded Mulberry32 PRNG lockstep stream).*
