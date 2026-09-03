# Portable request: container icons

Use this template when requesting one or more `container` icons. A container is
an independently recognizable outer icon with a protected centered region for
a separately authored sub icon.

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
Reference SVGs: <explicit selected files, or omit for a description-only request>
Output folder: <path, or omit to use work/<job>>

For each subject, deliver schema-version-2 editable JSON with iconType "container", the
empty design and ship SVG pair, complete QA evidence, and a non-shipping filled
preview using an accepted sub icon. Process only the listed subjects.
Use exact elements, inspect relevant local Lucide original/debug pairs, and
record applied construction principles. Do not add registry shapes or upload.
```

For one subject:

```text
Use docs/container-icons/SKILL.md to generate a container icon of <subject>.
Choose the accepted sub-icon keyshape that best preserves the container's
identity. Deliver schema-version-2 editable JSON, both empty profile sizes, QA evidence,
and a non-shipping filled preview.
```

When no folder is supplied, choose a dedicated `work/<job>` folder named from
the subject or reference stem.

For a handoff outside the repository, include this folder's skill, rules, and
generated profile plus the sub-icon skill and its rules/profile, the shared
rules, pipeline, selected input adapter, geometry and reference guide, and script inventory.
Preserve their relative paths and provide the referenced tooling so the
instructions remain usable.
