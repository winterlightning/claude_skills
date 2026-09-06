# Unlimited Shapes documentation

Choose the icon type first. Each folder contains its agent skill, type-specific
rules, generated numeric profile, and a portable request template. Built-in
defaults are **48×48 normal/main**, **32×32 sub**, and **64×64 container**, with
4px stroke. Sizes, strokes, keyshapes, validation and custom profile names are
configured in JSON through the [profile manager](shared/profile-configuration.md).
Output and acceptance review remain native 1:1 (1u = 1px); there is no half-size export.

| Type | Agent entrypoint | Rules | Numeric profile | Request template |
| --- | --- | --- | --- | --- |
| Complete standalone icon (`normal`) | [icons/SKILL.md](icons/SKILL.md) | [Normal rules](icons/rules.md) | [Normal profile](icons/profile.md) | [Normal request](icons/request.md) |
| Compact standalone or insertable icon (`sub`) | [sub-icons/SKILL.md](sub-icons/SKILL.md) | [Sub rules](sub-icons/rules.md) | [Sub profile](sub-icons/profile.md) | [Sub request](sub-icons/request.md) |
| Outer icon with an empty insertion slot (`container`) | [container-icons/SKILL.md](container-icons/SKILL.md) | [Container rules](container-icons/rules.md) | [Container profile](container-icons/profile.md) | [Container request](container-icons/request.md) |

An agent starts with the selected `SKILL.md` and reads its local rules and profile.
It loads another type only when the task also needs that type, such as the sub icon
used in a container preview. The three skills are role templates, not a fixed
enumeration of allowed types; custom named profiles use the shared pipeline and
[configuration guide](shared/profile-configuration.md). These are repository skill sources; pass the selected
entrypoint with the request when using an agent outside the repository.

## Where rules live

- Each type's `rules.md` owns its composition guidance and delivery contract.
  Normal badge layout, sub detail limits, and container clearance/preview rules
  belong in their respective folders.
- [Shared icon rules](shared/icon-rules.md) own the common geometry, paint,
  connections, and negative-space requirements, with stable rule IDs R1–R9.
- [`core/icon_profiles.json`](../core/icon_profiles.json) owns all numeric
  profile values. Each local `profile.md` and the
  [combined profile reference](shared/icon-profiles.md) are generated from it.
- The [shared pipeline](shared/icon-pipeline.md) owns command order and repair
  loops. Input adapters add only their scope and intake requirements.

Update the owning source when a rule changes. Regenerate Markdown profile
references after changing the profile JSON:

```bash
python3 core/generate_profile_assets.py
python3 core/generate_profile_assets.py --check
```

## Input workflows

There is one [shared pipeline](shared/icon-pipeline.md), with two intake modes:
**name + minimal description**, either **without references** or **with optional
SVG/PNG/other files**. Analyze the input and intended type, read that profile, plan
and author the icon, then pass **distance → holes/pinches → canvas/keyshape**.
Every repair restarts these three gates on regenerated output. All three fresh
passes, structural/grid/overlap prerequisites, and native-size visual approval
are required for completion. Text-only briefs need no fabricated SVG or detection.

| Input | Workflow |
| --- | --- |
| Name + minimal description, no references | The selected type's skill, then [brief-only intake](shared/icon-pipeline.md#brief-only-intake) |
| Name + minimal description + PNG/other/mixed references | The selected type's skill, then [reference-backed intake](shared/icon-pipeline.md#reference-backed-intake) |
| Exactly one supplied SVG | [Single-SVG adapter](shared/icon-execution-steps.md) |
| An explicitly selected SVG batch | [Batch adapter](shared/icon-batch-execution-steps.md) |
| Symbol-library `kind: "rework"` JSON | [Normal-icon rework](icons/rework.md) |
| Local manifest-based rework pack | [Local pack lane](icons/rework.md#local-manifest-pack-lane) |
| Symbol-library generation pack (`kind: "generate"`, per-symbol `icon_type.txt`) | [Generate skill](GENERATE_SKILL.md) |

The automated rework/upload wrapper produces normal icons. Sub and container
work use the same profile-aware core commands through their own skills.

## Shared references

- [Profile configuration and manager](shared/profile-configuration.md): edit the JSON source, manage validation/inheritance, and add custom profiles.

- [Editable geometry and Lucide references](shared/atomic-shapes.md): schema-version-2 elements, exact construction and on-demand reference retrieval.
- [Authoring techniques](shared/icon-authoring-guide.md): silhouette, joins, and optical review.
- [Script inventory](shared/scripts.md): commands, outputs, exit behavior, and type support.
- [Core scripts overview](shared/core-scripts-guide.md): tool navigation.
- [Hole and pinch QA](shared/qa-overlays-guide.md) and
  [repair examples](shared/negative-space-repair-examples.md): measurement and interpretation.
- [Portable single-SVG handoff](shared/README-svg-input-processing.md): a request for any declared type.

Run commands from the repository root. Keep job evidence and outputs under
`work/<job>/`, separate from maintained rules and source assets. Repair editable
geometry JSON, re-emit the native SVG and any same-size compatibility alias, and
recheck prerequisites and restart distance → holes → keyshape before delivery.
New contours require no registry extension or generated shape assets. Keep any
remote upload separate from local delivery and require explicit authorization.
