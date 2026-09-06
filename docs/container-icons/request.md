# Portable request: container icons

Use this template when requesting one or more `container` icons. A container is
an independently recognizable outer icon with a protected centered region for
a separately authored sub icon. Use the configured `container` profile (built-in
default 64×64px with 4px stroke). Use [the sub request](../sub-icons/request.md)
for its compatible unscaled insert and [the normal request](../icons/request.md)
for a main icon instead. Custom named profiles use
[profile configuration](../shared/profile-configuration.md).

The [skill](SKILL.md) selects the input lane, [rules.md](rules.md) owns
container-specific policy, [profile.md](profile.md) provides generated geometry,
and the [shared pipeline](../shared/icon-pipeline.md) owns commands and required
QA.

## Request to send

```text
Use docs/container-icons/SKILL.md to generate container icons for:
- <container subject>
- <another subject, optional>

Accepted sub-icon keyshape: <sub-profile token, or choose per subject>
For each subject, provide: <concept name> — <minimal description>.
References (optional): <selected SVG/PNG/other files, or none>
Output folder: <path, or omit to use work/<job>>

For each subject, deliver schema-version-2 editable JSON with iconType "container", the
empty canonical <name>.svg at the configured container canvas/stroke, complete QA
evidence, and a filled preview at that same native size. Use an unscaled insert
matching containerSlot.acceptedProfile and acceptedKeyshape. Resolve sizes,
keyshapes, slot and validation settings from core/icon_profiles.json; no half-size
container derivative.
Process only the listed subjects.
Analyze the input, read the selected profile, and plan the icon before drawing.
No-reference briefs need no synthetic source SVG or detector report.
After structural/grid/overlap prerequisites, pass distance → holes/pinches →
canvas/keyshape. Read each failing pair/zone/bounds, repair editable geometry,
regenerate, and restart at distance. All three must pass on the same final
SVG/profile before native-size visual approval; report blockers, never waive them.
Use exact elements, inspect relevant local Lucide original/debug pairs, and
record applied construction principles. Do not add registry shapes or upload.
```

For one subject:

```text
Use docs/container-icons/SKILL.md to generate a container icon of <subject>.
Choose the accepted sub-icon keyshape that best preserves the container's
identity. Deliver schema-version-2 editable JSON, the configured container-native
SVG, QA evidence, and a non-shipping filled preview at that same size. Author its
insert at the accepted profile's configured size and place it unscaled. Do not create half-size derivatives.
```

When no folder is supplied, choose a dedicated `work/<job>` folder named from
the subject or reference stem.

For a handoff outside the repository, include this folder's skill, rules, and
generated profile plus the sub-icon skill and its rules/profile, the shared
rules, pipeline, selected input adapter, geometry and reference guide, and script inventory.
Preserve their relative paths and provide the referenced tooling so the
instructions remain usable.
