# Redrawn queue page — offset 10

Frozen batch: 10 source UUIDs from the prior offset-10 fetch. User authorized drawing all visible compositions on 2026-09-22, resolving the prior interpretation holds. Current saved status and briefs were rechecked for every UUID; no newer generated state was found. Minus remains sub.

All ten were newly drawn. **Nine pass geometry validation with zero warnings. The perspective brick remains an invalid draft. No gallery export succeeded:** every targeted build was blocked by the pre-existing duplicate registry ID `stacked-paper-documents`, present in the container and solo families. No unrelated source was altered. Build error logs are beside this report. No combinations were saved; no API save failures or retry payloads.

## Per-source results

| UUID | Drawing | Checks | Python original |
|---|---|---|
| c6d7f6d7-a700-4894-830b-9788ba0a2a17 | Graffiti cloud | valid; 0 warnings; export blocked | [interlocking-graffiti-cloud](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/interlocking_graffiti_cloud_c6d7f6d7_a700_4894_830b_9788ba0a2a17.py) |
| 3e406d94-3472-495a-b48a-7dc0d21a13ed | Gymnast on bar | valid; 0 warnings; export blocked | [gymnast-supported-on-horizontal-bar](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/gymnast_supported_on_horizontal_bar_3e406d94_3472_495a_b48a_7dc0d21a13ed.py) |
| 757a7e35-7ab6-4777-857e-44cd9f41831d | Snowflake and water | valid; 0 warnings; export blocked | [snowflake-over-water-waves](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/snowflake_over_water_waves_757a7e35_7ab6_4777_857e_44cd9f41831d.py) |
| 9c89e718-df3d-451b-808f-bb9daab2e5b2 | Cleaning worker | valid; 0 warnings; export blocked | [cleaning-worker-with-upright-broom](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/cleaning_worker_with_upright_broom_9c89e718_df3d_451b_808f_bb9daab2e5b2.py) |
| d3d86e97-b873-48ff-bd6b-fc4456184a6e | Speaking person | valid; 0 warnings; export blocked | [speaking-profile-with-empty-bubble](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/speaking_profile_with_empty_bubble_d3d86e97_b873_48ff_bd6b_fc4456184a6e.py) |
| 2f1ae9d4-7c42-400d-8760-d69f1f5f0abd | Blood drop and ring | valid; 0 warnings; export blocked | [blood-drop-with-evidence-ring](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/blood_drop_with_evidence_ring_2f1ae9d4_7c42_400d_8760_d69f1f5f0abd.py) |
| 770b8052-e66d-401b-ae0d-9284719da14f | Rounded minus | valid; 0 warnings; export blocked | [rounded-horizontal-subtraction-mark](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/sub/rounded_horizontal_subtraction_mark_770b8052_e66d_401b_ae0d_9284719da14f.py) |
| 8c0da42a-e577-481a-a50e-84f0e8648aae | Toy brick — DRAFT | invalid; 2 warnings; export blocked | [four-stud-perspective-toy-brick](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/_draft_four_stud_perspective_toy_brick_8c0da42a_e577_481a_a50e_84f0e8648aae.py) |
| 6e501462-4458-4ee8-918b-3b9b1c8dded4 | Left profile and brain | valid; 0 warnings; export blocked | [left-profile-with-lobed-brain](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/left_profile_with_lobed_brain_6e501462_4458_4ee8_918b_3b9b1c8dded4.py) |
| 0231a044-ecb1-470e-bcc3-8a45ccdc5d4a | Right profile and brain | valid; 0 warnings; export blocked | [right-profile-with-folded-brain](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/right_profile_with_folded_brain_0231a044_ecb1_470e_bcc3_8a45ccdc5d4a.py) |

## Design and review notes

- Graffiti: HRECT_L fits the broad abstract lobed silhouette. One internal seam retains the interlocking character; no lettering was invented. Lucide cloud supplied smooth-lobe construction principles.
- Gymnast: VRECT_L fits supports and body. Read as supported upright at the bar, with one torso and two legs. Human reference supplies circular head and simple limbs; exact detached head-to-torso ink gap is 4.
- Snow/water: SQUARE contains one simple snowflake over two wave rows. Small branches and the third wave row were omitted for separation and native legibility.
- Worker: HRECT_L gives broom room beside the portrait. Cap brim, circular head, smooth shoulders and trapezoid broom remain; shirt/collar omitted. The detached head/shoulder gap is 4.
- Speaker: HRECT_L retains the right-facing head, projecting nose, neck and empty upper-right speech bubble. Ear/lip detail omitted; bubble narrowed to preserve clearance. Lucide message-square informs the tail.
- Drop/ring: HRECT_L retains the interrupted drop and both concentric ring boundaries. No invented fingerprint added. Lucide droplet informs contour flow.
- Minus: SUB32 HRECT_S with semicircular ends and an open interior. It is thicker relative to its length than the source to satisfy the compact profile.
- Brick: HRECT_L perspective redraw preserves four studs and two side faces. Revised thickness clears parallel-edge checks, but remaining stud spacing is 6.05–7 rather than required 8 centerline units; rear studs intersect the body outline. Kept as an explicitly unexported draft, with earlier drafts intact. Lucide toy-brick informed the hierarchy.
- Brain profiles: SQUARE provides a broader skull and visible lobed intrinsic brain, retaining source direction and a short descending extension. Right-facing version includes one simplified fold; fine anatomy omitted. Human and Lucide brain references informed smooth curves and lobe construction.

Actual native light/dark renders inspected. The nine passing drawings retain recognizable silhouettes and separated major parts. Fine anatomy remains deliberately simplified; the right-brain fold is dense at native size. QA sheets use the repository contact-sheet renderer. SVGs here are direct Python-model renderings for review, not published gallery exports.

Existing underscore-prefixed drafts cannot be found by create_variant.py, which only accepts registered IDs; independently named redraw modules preserve all parents without modifying them. Authorship is gpt-6. Source metadata, full UUIDs and source paths retained.

Remaining work: resolve the unrelated duplicate registry ID before targeted builds can export the nine passing drawings; redesign the brick spacing before export.
