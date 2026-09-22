# Solo queue review — offset 10

Requested offset: **10**. Returned item count: **10**. Fixed response order preserved; no replacement items fetched.

**Outcome:** 0 generated, 0 verified prepared combinations, 5 interpretation holds, 1 family deferral, 4 unresolved subjects with existing drafts. No status or brief writes were attempted, so there are no save failures or retry payloads. No existing Python originals, source SVGs, or published outputs were changed.

Each reference had its current status and saved brief read from http://localhost:8000 immediately before intake. All ten currently report TODO; that does not resolve the saved holds or draft quality issues. Current records and renders are saved alongside this report.

## 1. Gymnast on Horizontal Bar
- UUID: `3e406d94-3472-495a-b48a-7dc0d21a13ed`
- Source: `pictographic-primitives/_uncategorized_21/gymnastics acrobatic hanging person_3e406d94-3472-495a-b48a-7dc0d21a13ed.svg`
- Outcome: **Interpretation hold**
- Finding: Head and bar are visible, but the three lower strokes do not establish the limb pose. Existing hold preserved.

## 2. Snowflake and Water Waves
- UUID: `757a7e35-7ab6-4777-857e-44cd9f41831d`
- Source: `pictographic-primitives/_uncategorized_23/ice water_757a7e35-7ab6-4777-857e-44cd9f41831d.svg`
- Outcome: **Interpretation hold**
- Finding: Snowflake above water can signify a cold modifier or a scene. Existing hold preserved; no split asserted.

## 3. Cleaning Worker with Broom
- UUID: `9c89e718-df3d-451b-808f-bb9daab2e5b2`
- Source: `pictographic-primitives/_uncategorized_23/janitor_9c89e718-df3d-451b-808f-bb9daab2e5b2.svg`
- Outcome: **Interpretation hold**
- Finding: Broom overlaps the capped bust without a gripping hand. Existing equipment-versus-modifier hold preserved.

## 4. Speaking Person with Speech Bubble
- UUID: `d3d86e97-b873-48ff-bd6b-fc4456184a6e`
- Source: `pictographic-primitives/_uncategorized_25/linguist_d3d86e97-b873-48ff-bd6b-fc4456184a6e.svg`
- Outcome: **Interpretation hold**
- Finding: Speech bubble beside speaking profile retains the existing scene-versus-modifier hold.

## 5. Blood Drop Target
- UUID: `2f1ae9d4-7c42-400d-8760-d69f1f5f0abd`
- Source: `pictographic-primitives/_uncategorized_26/luminal evidence pinger print blood_2f1ae9d4-7c42-400d-8760-d69f1f5f0abd.svg`
- Outcome: **Interpretation hold**
- Finding: Empty ring overlaps the drop; evidentiary meaning remains unconfirmed. Existing hold preserved.

## 6. Rounded Horizontal Minus Sign
- UUID: `770b8052-e66d-401b-ae0d-9284719da14f`
- Source: `pictographic-primitives/_uncategorized_27/minimize_770b8052-e66d-401b-ae0d-9284719da14f.svg`
- Outcome: **Family deferred**
- Finding: Saved family is sub, confirmed by an authoritative classification in the fetched queue. Ineligible for solo drawing; source unchanged.

## 7. Four Stud Toy Building Brick
- UUID: `8c0da42a-e577-481a-a50e-84f0e8648aae`
- Source: `pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg`
- Outcome: **Unresolved draft / concurrent work**
- Finding: Existing top-view draft validates but visually reads as a die or button. Perspective draft appeared during this pass and fails parallel-edge spacing (7.15542 versus 8), stud spacing (4.26147 versus 8), and intersection warnings. Neither exported; existing originals untouched.

## 8. Human Head with Brain
- UUID: `6e501462-4458-4ee8-918b-3b9b1c8dded4`
- Source: `pictographic-primitives/_uncategorized_28/neurobiologist_6e501462-4458-4ee8-918b-3b9b1c8dded4.svg`
- Outcome: **Unresolved drafts**
- Finding: Two existing originals match this UUID. VRECT_L version validates but loses lobes/stem at native size. SQUARE version retains lobes but face-to-brain centerline gap is 5.30276 versus required 8. Neither exported or edited.

## 9. Human Head with Brain
- UUID: `0231a044-ecb1-470e-bcc3-8a45ccdc5d4a`
- Source: `pictographic-primitives/_uncategorized_28/neuropathologist_0231a044-ecb1-470e-bcc3-8a45ccdc5d4a.svg`
- Outcome: **Unresolved drafts**
- Finding: Two existing originals match this UUID. VRECT_L version validates but lacks recognizable folded brain and descending stem. SQUARE version fails face-to-brain centerline gap, 5.30276 versus required 8. Neither exported or edited.

## 10. Human legs wearing pantyhose
- UUID: `f422872b-42cf-4b74-aa1f-bf870f557d7a`
- Source: `pictographic-primitives/_uncategorized_29/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg`
- Outcome: **Unresolved draft**
- Finding: VRECT_M candidate fails exact keyshape bounds and standing/rear and rear/cross spacing (3.82933 and 3.85064 versus required 8). Native render crowds the knee and crossing; not exported or edited.

## Validation and visual evidence

See `draft-validation.json` for complete reports and source module paths. `draft-review.png` contains actual 48px light/dark renders alongside 2× enlargements of all seven existing candidates. These are draft inspections, not completed build reviews. No candidate was built or claimed present in the passing manifest.

The queue skill permits ambiguous references to be skipped and requires zero-warning validation plus visual acceptance before completion. The distilled skill also requires ambiguous existing source matches to be resolved before editing. Existing editorial holds and competing originals are preserved.
