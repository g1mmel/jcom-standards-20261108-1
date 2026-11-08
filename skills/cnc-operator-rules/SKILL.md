---
name: cnc-operator-rules
description: Binding operator rules for the C:\cnc_rev RTS project (canon precedence, delegation, naming, no-delete, no-deploy). Load before any decision, edit or dispatch in C:\cnc_rev, or when unsure what is allowed.
---

# cnc_rev operator rules (binding)

**Operator rulings are LOCKED and cited.** Everything the operator said is in `canon/OPERATOR-RULINGS.md` (source of truth: `data/canon/operator-rulings.json`, sealed by sha256). Cite as `[OR-nnn]` wherever you apply one. Never edit, soften or drop a quote, id or LOCKED status. A ruling beats other canon: log the conflict, do not "fix" the ruling. New rulings: append to the JSON, then `node scripts/operator-rulings.mjs render`, `seal`, `check`. Run `check` before reporting done on any lane that touches canon, rules or briefs.


Source of truth: `HANDOFF.md` section 1, `TRUTH.md`, `docs/DECISIONS.md` (ADR-001..011). If this file and those disagree, they win. Fix this file.

- **Executive role.** Delegate. Do not do hands-on work, screenshots or manual checks; the QA lane does those. Keep driver (Claude) usage low. Gemini/agy and grok are free. Sol (OpenRouter) may cost money: use only for judging and review.
- **Writing style.** Punchy, clear, concise, like the operator's songs (operator ruling 2026-10-14; replaces the older ASD-STE100 rule in HANDOFF.md). No filler. Short lines that land. Specs stay exact. Applies to briefs, reports, docs and canon. For a voice pass, ask torch0019 over the relay.
- **Canon.** torch's game CONCEPTS are binding; his engine and code are not (ADR-001). Precedence: `canon/CANON-INDEX.md`.
- **Concept test (ADR-009).** If it happens in real life and it is terrible, include it, with a source.
- **Variables, never hardcode (ADR-010).** Use the `cnc-add-variable` skill. Agents settle design ambiguity among themselves. Escalate only values calls.
- **Factions.** Runtime names: JSLC / AoI / Penguins. The UN is an antihero. AoI "old school" is a character attitude only, not a gameplay bonus.
- **No video cutscenes.** Operator ban (2026-10-14). Never run `cinematics/record.mjs`, render MP4/WebM, or dispatch a video lane. Text scripts and storyboards are fine. Drop any video task from briefs.
- **Assets.** Retail and mod assets (ZH, Generals Universe, GenEvo, C&C3, RA3) are private test content. Never raise licensing.
- **Platform.** Desktop web first. UI must still work at 393x852. Phone perf budget is deferred.
- **Never deploy** to jewishspacelasercommand.com. torch owns it. Send proposals to torch as files.
- **Never delete.** Move to `_quarantine/<date>/` and wait for operator approval.
- **Git.** Workers never run git commit/push/checkout/reset/stash. Only `scripts/autopush.ps1` commits (check it is running).
- **Protected dirs.** Never edit in place: `_ref/jslcnc`, `C:\z4yin\cnc-zh_assets`, `\\NAI-SV2\`, `D:\ea\`. Copy first.
- **Sim tick.** Target 30 Hz (ADR-004); `TICK_HZ` is the one switch.
