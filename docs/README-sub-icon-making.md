# Portable handoff: sub icons

Use this template when requesting one or more standalone `sub` icons. A sub
icon is not a corner badge and is not a completed normal icon scaled down.

The normative contract lives in [icon-types.md](icon-types.md), exact profile
values are generated in [generated/icon-profiles.md](generated/icon-profiles.md),
and all commands are in the shared [icon pipeline](icon-pipeline.md). This page
adds only the sub-icon request contract.

## Sub-icon constraints

- Declare `"iconType": "sub"` in every editable source.
- Compose directly on the sub design profile. Reuse registered atoms only when
  they preserve the strongest silhouette; add a generic parametric atom rather
  than compromise a small icon's recognizability.
- Prefer one dominant silhouette and no more than two internal
  identity-bearing features.
- Select a sub-profile keyshape from the dominant whole-icon silhouette.
- Keep distinct stroke centerlines at least 3u apart; the 4u normal/container
  floor does not apply to the 32×32 sub profile.
- Inspect recognition and negative space at the exact sub ship size.
- Use the same profile-aware emitter and validators as every other icon type.

Do not use the historical `output_subicon/build-sub-icons.py` helper for new
work. It remains only for reproducing old examples; the shared core pipeline is
the supported route.

## Request to send

```text
Follow the repository's canonical icon pipeline and generate sub icons for:
- <subject or short description>
- <another subject, optional>

Output folder: <path, or omit to use generated/sub-icons>

For each subject, deliver editable atomic JSON with iconType "sub", the sub
design and ship SVG pair, all required QA evidence, and a true-size preview.
Process only the listed subjects and keep each independently recognizable.
```

For one subject:

```text
Follow the canonical icon pipeline and generate a sub icon of <subject>.
Deliver editable atomic JSON, both profile sizes, QA evidence, and a true-size
preview.
```

If this file is sent outside the repository, include `icon-pipeline.md`,
`icon-types.md`, `icon-rules.md`, `atomic-shapes.md`, and the generated profile
reference so links and machine-defined values remain available.
