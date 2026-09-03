# Unlimited Shapes documentation

Choose the icon type first. Each folder contains its agent skill, type-specific
rules, generated numeric profile, and a portable request template.

| Type | Agent entrypoint | Rules | Numeric profile | Request template |
| --- | --- | --- | --- | --- |
| Complete standalone icon (`normal`) | [icons/SKILL.md](icons/SKILL.md) | [Normal rules](icons/rules.md) | [Normal profile](icons/profile.md) | [Normal request](icons/request.md) |
| Compact standalone or insertable icon (`sub`) | [sub-icons/SKILL.md](sub-icons/SKILL.md) | [Sub rules](sub-icons/rules.md) | [Sub profile](sub-icons/profile.md) | [Sub request](sub-icons/request.md) |
| Outer icon with an empty insertion slot (`container`) | [container-icons/SKILL.md](container-icons/SKILL.md) | [Container rules](container-icons/rules.md) | [Container profile](container-icons/profile.md) | [Container request](container-icons/request.md) |

An agent starts with the selected `SKILL.md` and reads its local rules and profile.
It loads another type only when the task also needs that type, such as the sub icon
used in a container preview. These are repository skill sources; pass the selected
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

Update the owning source when a rule changes. Regenerate profile pages and the
browser mirror after changing the profile JSON:

```bash
python3 core/generate_profile_assets.py
python3 core/generate_profile_assets.py --check
```

## Input workflows

| Input | Workflow |
| --- | --- |
| Subject or short description | The selected type's skill, then [shared intake](shared/icon-pipeline.md#0-route-the-request) |
| Exactly one supplied SVG | [Single-SVG adapter](shared/icon-execution-steps.md) |
| An explicitly selected SVG batch | [Batch adapter](shared/icon-batch-execution-steps.md) |
| Symbol-library `kind: "rework"` JSON | [Normal-icon rework](icons/rework.md) |
| Local manifest-based rework pack | [Local pack lane](icons/rework.md#local-manifest-pack-lane) |

The automated rework/upload wrapper produces normal icons. Sub and container
work use the same profile-aware core commands through their own skills.

## Shared references

- [Editable geometry and Lucide references](shared/atomic-shapes.md): schema-version-2 elements, exact construction and on-demand reference retrieval.
- [Authoring techniques](shared/icon-authoring-guide.md): silhouette, joins, and optical review.
- [Script inventory](shared/scripts.md): commands, outputs, exit behavior, and type support.
- [Core scripts overview](shared/core-scripts-guide.md): tool navigation.
- [Hole and pinch QA](shared/qa-overlays-guide.md) and
  [repair examples](shared/negative-space-repair-examples.md): measurement and interpretation.
- [Portable single-SVG handoff](shared/README-svg-input-processing.md): a request for any declared type.

Run commands from the repository root. Keep job evidence and outputs under
`work/<job>/`, separate from maintained rules and source assets. Repair editable
geometry JSON, re-emit both SVG sizes, and rerun the affected checks before delivery.
New contours require no registry extension or generated shape assets. Keep any
remote upload separate from local delivery and require explicit authorization.
