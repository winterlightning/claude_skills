# Portable request: sub icons

Use this template when requesting one or more standalone `sub` icons. A sub
icon uses the configured `sub` profile (built-in default 32×32px with 4px stroke),
not a corner badge or a completed normal icon scaled down. For main icons use
[the normal request](../icons/request.md); for outer containers use
[the container request](../container-icons/request.md). Custom named profiles
use [profile configuration](../shared/profile-configuration.md).

The [skill](SKILL.md) selects the input lane, [rules.md](rules.md) owns
sub-specific policy, [profile.md](profile.md) provides generated geometry, and
the [shared pipeline](../shared/icon-pipeline.md) owns commands and required QA.

## Request to send

```text
Use docs/sub-icons/SKILL.md to generate sub icons for:
- <subject or short description>
- <another subject, optional>

Reference SVGs: <explicit selected files, or omit for a description-only request>
Output folder: <path, or omit to use work/<job>>

For each subject, deliver schema-version-2 editable JSON with iconType "sub",
canonical <name>.svg at the configured sub canvas/stroke, all required QA evidence,
and a preview at that same native size. Resolve validation settings from
core/icon_profiles.json. Do not produce or review a half-size derivative.
Process only the listed subjects and keep each independently recognizable.
Use exact elements, inspect relevant local Lucide original/debug pairs, and
record applied construction principles. Do not add registry shapes or upload.
```

For one subject:

```text
Use docs/sub-icons/SKILL.md to generate a sub icon of <subject>.
Deliver schema-version-2 editable JSON, the configured sub native SVG,
QA evidence, and a preview at that same size. Resolve canvas, stroke, keyshapes,
and validation from the JSON profile. Do not produce a half-size version.
```

When no folder is supplied, choose a dedicated `work/<job>` folder named from
the subject or reference stem.

For a handoff outside the repository, include this folder's skill, rules, and
generated profile plus the shared rules, pipeline, selected input adapter,
geometry and reference guide, and script inventory. Preserve their relative paths and provide
the referenced tooling so the instructions remain usable.
