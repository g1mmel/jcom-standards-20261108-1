# Research log: ea-18g-growler

- Start local time: 2026-10-14T15:14:39-04:00
- End local time: 2026-10-14T15:27:18-04:00
- Search count: 12
- Fetch count: 8 successful page reads used for the Growler, plus the E/F, legacy Hornet, FlightGlobal, and gun-sheet pages used for comparison. Failed fetches are listed.

## Queries

1. site:navy.mil EA-18G Growler fact file length wingspan crew
2. site:navair.navy.mil EA-18G Growler product specifications ALQ-218
3. Boeing EA-18G Growler fact sheet dimensions wingtip pods ALQ-218 gun removed
4. EA-18G Growler wingspan with ALQ-218 wingtip pods versus F/A-18E span
5. Congressional Research Service F/A-18E/F Super Hornet EA-18G Growler background dimensions
6. EA-18G Growler ALQ-218 wingtip receiver gun bay pallet ALQ-227 nine weapon stations
7. EA-18G Growler folded wingspan width wings folded ALQ-218 antennas
8. site:navy.mil EA-18G "ALQ-218" wingtip OR "wing tip" receiver pod
9. EA-18G Growler AN/ALQ-249 Next Generation Jammer Mid-Band pod stations crew pilot EWO
10. RAAF EA-18G Growler specifications length wingspan height weight crew
11. EA-18G "gun bay" pallet "20 mm" OR cannon OR M61 removed OR deleted Boeing
12. EA-18G INCANS interference cancellation system jamming communications ALQ-227

Query 5 is shared with the Super Hornet log because the query text names both aircraft. It did not return a CRS dimension table. No fetched page gave a folded span or a numeric pod-versus-rail span delta.

## Fetches

Successful:

1. https://www.navair.navy.mil/product/EA-18G-Growler — title "EA-18G Growler | NAVAIR". Gave the F/A-18F platform, crew of two, two F414-GE-400 at 22,000 lb (9,977 kg), length 60.2 ft (18.5 m), height 16 ft (4.87 m), span 44.9 ft (13.68 m), empty 33,094 lb, recovery 48,000 lb, combat range 850+ nm, armament of two AIM-120, two AGM-88, and three ALQ-99. Also the conflicting first-flight lines and a right-wing NGJ-MB caption.
2. https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2166036/ea-18g-growler-airborne-electronic-attack-aircraft — title "EA-18G Growler Airborne Electronic Attack Aircraft". Direct web_fetch was access denied. open_page succeeded. Same specification card, plus ALQ-218, ALQ-99, ALQ-227, Joint Tactical Terminal, APG-79, and the September 2021 "final development" line for AN/ALQ-249. Unit cost $67 million against NAVAIR's $68 million.
3. https://www.boeing.com/defense/fighters-and-bombers/fa-18-super-hornet-and-ea-18-growler — title "F/A-18 Super Hornet & EA-18 Growler". Growler block: 60.2 ft (18.3 m), 44.9 ft (13.7 m), 16 ft (4.9 m), recovery 48,000 lb (21,772.4 kg), Mach 1.8, spot factor 1.23, thrust 44,000 lb. The Super Hornet block on the same page is 60.2 ft, Mach 1.6, and 17,000 lb per engine.
4. https://www.geaerospace.com/military-defense/engines/f414 — title "F414 Engine | GE Aerospace". Gave the Growler application and the 22,000 lb class.
5. https://www.aviationtoday.com/2008/03/01/teeth-of-the-growler/ — title "Teeth of the Growler". Gave wingtip ALQ-218(V)2 pods in place of missile rails, nose pallet replacing the 20 mm cannon, up to five ALQ-99 pods, ALQ-227, INCANS, pilot and ECMO, March 2006 podded-E test, August 2006 first purpose-built G, about 1,400 lb, 2,500 ft of cable, and 66 antennas.
6. https://www.navair.navy.mil/product/ALQ-99-Tactical-Jamming-System — title "ALQ-99 Tactical Jamming System | NAVAIR". External pods on the EA-18G, retained until NGJ increments reach full operational capability.
7. https://www.navair.navy.mil/product/Next-Generation-Jammer — title "Next Generation Jammer | NAVAIR". AN/ALQ-249 mid-band external pods, Milestone C 2021, LRIP III March 2023, first production pods July 2023. Low-band still in EMD.
8. https://www.l3harris.com/all-capabilities/ea-18g-interference-cancellation-system-incans — title "EA-18G Interference Cancellation System (INCANS)". Function only. No station.

Comparison pages also read: NAVAIR F/A-18E/F, NAVAIR F/A-18 A-D, FlightGlobal 20 January 1999, and the GD-OTS E/F gun sheet. URLs are in the Super Hornet research log.

Failed, and what replaced them:

- https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2166036/ea-18g-growler-airborne-electronic-attack-aircraft — web_fetch access denied, replaced by open_page, which succeeded.
- https://www.cnatra.navy.mil/tw6/vt86/aircraft-EA18G.asp — fetch failed. Search extract only. Not used as a certified figure. The extract repeated 60.2 ft, 16 ft, 44.9 ft, empty 33,094 lb, recovery 48,000 lb, and said nine weapon stations and wingtip pods.
- https://www.airforce.gov.au/aircraft/ea-18g-growler — DNS failure. Search extract only. Not used as a certified figure. The extract showed 18.3 m, 4.9 m, 13.7 m, empty 15,011 kg, Mach 1.6, and crew "Pilot" and "Electronic Warfare Officer". Mach 1.6 would disagree with Boeing's Growler Mach 1.8 if the page had opened.
- https://web.archive.org/web/20131008041538/http://www.boeing.com/assets/pdf/defense-space/military/ea18g/docs/EA-18G_overview.pdf — archive shell only. The search extract of that PDF showed empty 33,094 lb, nine weapon stations, and a gun-bay pallet. Not used as a certified figure because the PDF did not open.
- Folded-span query did not produce a fetched page with a folded width. Secondary snippets that said about 30 ft or 32 ft were not opened and were not used.

## Numbers that failed the two-source test

- 60.2 ft versus the printed 18.5 m on the NAVAIR and Navy fact-file cards. Boeing's 18.3 m is a rounding, not a second measurement of a different airframe.
- NAVAIR E/F length 60.3 ft versus Growler length 60.2 ft. Boeing prints 60.2 ft for both.
- Empty weight 33,094 lb is repeated by NAVAIR and the Navy fact file, same programme office. Boeing's current card does not repeat it. Treated as official text, not as two independent weighings.
- Recovery weight 48,000 lb is on the official cards and on Boeing. That one passed.
- Maximum takeoff weight, folded span, wing area, internal fuel, weapon-station count, and pod-versus-rail span delta: not public on fetched pages.
- "Up to five" ALQ-99 pods versus the official armament line of three. Both printed. Not averaged.
- Unit cost $67 million versus $68 million.
- First flight October 2004 versus August 2006, including both lines on the same official pages. Aviation Today supports August 2006 for the purpose-built jet and March 2006 for a podded F/A-18E.
- Mach 1.8 is Boeing only. The RAAF Mach 1.6 extract was not a successful fetch.
- 1,400 lb, 2,500 ft of cable, 66 antennas, wingtip station of the ALQ-218, and cannon replacement: Aviation Today only. The official armament line omits a gun but does not itself say the gun was removed.
- ALQ-218 wingtip location was not on the NAVAIR specification card. The fact file names the receiver and does not give the station.
- Spot factor 1.23: Boeing only.
- Nine weapon stations: search extracts only. Not used.
- Knowledge-pack figures for folded span 9.98 m, station butt lines, and pivot angles: not re-verified. Not copied.

## Contradictions versus the base dossier

- Every legacy dimension on the base card is the wrong airplane. The Growler cards are 60.2 ft, 44.9 ft, and 16 ft, not 17.070 m, 12.310 m, and 4.670 m.
- Base MTOW 23,541 kg is the legacy Hornet's pounds converted. Growler MTOW is not public. Published Growler weights are empty 33,094 lb and recovery 48,000 lb.
- Base APG AESA as a generic fit, EOTS fairing, distributed aperture, and internal bays do not appear on Growler pages. The fact file names only the APG-79.
- Base wingtip ESM pods are wrong for the legacy Hornet and wrong for the E. They are right in kind for the G only as AN/ALQ-218 receiver pods, and the station is single-source.
- Base nose gun and dorsal speed brake. The Growler source that describes the nose says the cannon is replaced. The dorsal brake is an E/F deletion inherited from the FlightGlobal description, not a Growler-specific measurement.
- Base single-seat scene graph. The G is two-seat, on the F platform.

## Game conflicts

- Game 18.5 / 13.68 / 4.87 m matches the NAVAIR and Navy fact-file metre labels and not their feet, and not Boeing's metres.
- The source note's phrase "outer mould line" is not on the cited NAVAIR page. Boeing prints identical feet for both aircraft. NAVAIR's E/F length line is 60.3 ft and the Growler line is 60.2 ft.
- Published span feet are the same for the E and the G. A different span caused by the wingtip pods is not public, so the shared width is consistent with the cards and is not a measured proof that the pods match the missile rails.
- The E game note of folded span 32.6 ft was not found for the G.
- Null mass omits the published empty weight of 33,094 lb. It does not assert a conflicting mass.
