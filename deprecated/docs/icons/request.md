# Portable request: normal icons

Use this template for complete standalone `normal`/main icons. Its built-in
default is 48×48px with 4px stroke; current JSON configuration overrides those
numbers. For compact symbols use [the sub request](../sub-icons/request.md); for
outer containers use [the container request](../container-icons/request.md).
For a custom named profile, use [profile configuration](../shared/profile-configuration.md). The
[skill](SKILL.md) selects the input lane, [rules.md](rules.md) owns normal-specific
policy, [profile.md](profile.md) provides generated geometry, and the
[shared pipeline](../shared/icon-pipeline.md) owns commands and required QA.

## Request to send

```text
Use docs/icons/SKILL.md to create normal icons for:
- <subject or short description>
- <another subject, optional>

For each subject, provide: <concept name> — <minimal description>.
References (optional): <selected SVG/PNG/other files, or none>
Output folder: <path, or omit to use work/<job>>
Composite badge, if needed: <modifier and intended meaning>

For each subject, deliver schema-version-2 editable JSON with iconType "normal", the
canonical <name>.svg at the configured normal canvas/stroke, all required QA
evidence, and a preview at the same native size. Resolve validation settings from
core/icon_profiles.json. Do not produce or review a half-size derivative.
Process only the listed subjects and selected references.
Analyze the input, read the selected profile, and plan the icon before drawing.
No-reference briefs need no synthetic source SVG or detector report.
After structural/grid/overlap prerequisites, pass distance → holes/pinches →
canvas/keyshape. Read each failing pair/zone/bounds, repair editable geometry,
regenerate, and restart at distance. All three must pass on the same final
SVG/profile before native-size visual approval; report blockers, never waive them.
Use exact elements, inspect relevant local Lucide original/debug pairs, and
record applied construction principles. Do not add registry shapes or upload.
```

For exactly one supplied SVG:

```text
Use docs/icons/SKILL.md to remake the attached SVG as one normal icon.
Preserve the reference and process only that SVG. Deliver schema-version-2 editable JSON,
the configured normal native SVG, required QA evidence, and a preview at that
same size. Resolve canvas, stroke, keyshapes, and validation from the JSON profile.
Do not produce a half-size version.
```

When no folder is supplied, choose a dedicated `work/<job>` folder named from
the subject or reference stem. For a local manifest pack or symbol-library
payload, use the matching lane in [rework.md](rework.md). For example:

```text
Use docs/icons/SKILL.md and the local pack lane to rework every symbol listed
in <pack-folder>/manifest.json. Preserve the manifest and prototypes. Author
schema-version-2 normal editable sources using the configured canvas/stroke and
validation settings, build and review the native manifest delivery files, and return QA evidence plus the source/output gallery. Do not upload.
```

For a handoff outside the repository, include this folder's skill, rules, and
generated profile plus the shared rules, pipeline, selected input adapter,
geometry and reference guide, and script inventory. Preserve their relative paths and provide
the referenced tooling so the instructions remain usable.
