# Solo queue offset 10 — review report

Requested offset **10**; returned **10 items**, total at fetch **75**. Frozen UUID order is in `ids.json`. No replacement page fetched. Local gallery: http://localhost:8000.

Read both current status and saved-brief endpoints for each UUID; snapshots retained alongside this report. All status records were absent (default TODO); seven remains saved as sub. Actual source SVGs were rendered and visually inspected in `references.png`.

**Results: 0 generated/exported; 0 verified combinations; 6 interpretation holds; 1 family defer; 3 unresolved existing drafts.** No saves failed: no classification or component save was attempted, and there are no retry payloads. No original, editorial brief, gallery state, or build output was changed. Existing drafts were inspected and revalidated, not revised or built.

| UUID | Subject | Result |
|---|---|---|
| c6d7f6d7-a700-4894-830b-9788ba0a2a17 | Cloudlike graffiti | Unresolved: abstract lobes versus stylized lettering; exact text not established. Existing hold preserved. |
| 3e406d94-3472-495a-b48a-7dc0d21a13ed | Gymnast at horizontal bar | Unresolved: the vertical strokes do not establish an anatomical pose. Existing hold preserved. |
| 757a7e35-7ab6-4777-857e-44cd9f41831d | Snowflake and water | Unresolved: cold-state modifier versus natural snow/water scene. Existing hold preserved. |
| 9c89e718-df3d-451b-808f-bb9daab2e5b2 | Cleaning worker with broom | Unresolved: equipment portrait versus separate occupation modifier; no grip visible. Existing hold preserved. |
| d3d86e97-b873-48ff-bd6b-fc4456184a6e | Speaking person and bubble | Unresolved: natural speech scene versus reusable speech modifier. Existing hold preserved. |
| 2f1ae9d4-7c42-400d-8760-d69f1f5f0abd | Blood drop and ring | Unresolved: empty ring meaning and its relationship to the drop remain unidentified. Existing hold preserved. |
| 770b8052-e66d-401b-ae0d-9284719da14f | Rounded minus sign | Skipped for this solo run: saved family is sub, following authoritative user classification; saved brief explicitly defers to icon-sub. |
| 8c0da42a-e577-481a-a50e-84f0e8648aae | Four-stud toy brick | Existing VRECT_L draft validates valid, zero warnings. Native light/dark review fails: looks like a die/button; protruding studs and perspective are absent. No export. |
| 6e501462-4458-4ee8-918b-3b9b1c8dded4 | Left profile with brain | Existing VRECT_L draft validates valid, zero warnings. Native light/dark review fails: brain reads as a small loop, losing lobes and descending extension. Anatomical organ is intrinsic, not a container combination. No export. |
| 0231a044-ecb1-470e-bcc3-8a45ccdc5d4a | Right profile with brain | Existing VRECT_L draft validates valid, zero warnings. Native light/dark review fails: brain lacks folds and stem; not sufficiently distinct from the left-profile draft. No export. |

## Evidence and limitations

The three existing drafts remain excluded from registry discovery by their `_draft_` filenames. Validation descriptions and actual native 48px light/dark renders are retained here. These are draft reviews, not successful build or manifest verification. Previous unsuccessful layout attempts are documented in `../solo-queue-offset-20-2026-09-21/report.md`; this run reconfirms those visual blockers without duplicating or overwriting the originals.

The queue skill says: “If the reference cannot be inspected or its interpretation remains ambiguous, report that limitation and skip drawing this item.” That applies to the first six sources. No combination classification was forced.
