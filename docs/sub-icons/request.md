# Portable request: sub icons

Use this template when requesting one or more standalone `sub` icons. A sub
icon is not a corner badge and is not a completed normal icon scaled down.

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

For each subject, deliver schema-version-2 editable JSON with iconType "sub", the sub
design and ship SVG pair, all required QA evidence, and a true-size preview.
Process only the listed subjects and keep each independently recognizable.
Use exact elements, inspect relevant local Lucide original/debug pairs, and
record applied construction principles. Do not add registry shapes or upload.
```

For one subject:

```text
Use docs/sub-icons/SKILL.md to generate a sub icon of <subject>.
Deliver schema-version-2 editable JSON, both profile sizes, QA evidence, and a true-size
preview.
```

When no folder is supplied, choose a dedicated `work/<job>` folder named from
the subject or reference stem.

For a handoff outside the repository, include this folder's skill, rules, and
generated profile plus the shared rules, pipeline, selected input adapter,
geometry and reference guide, and script inventory. Preserve their relative paths and provide
the referenced tooling so the instructions remain usable.
