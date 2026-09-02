# Portable handoff: container icons

Use this template when requesting one or more `container` icons. A container is
an independently recognizable outer icon with a protected centered region for
a separately authored sub icon.

The normative contract lives in [icon-types.md](icon-types.md), exact profile
and slot values are generated in
[generated/icon-profiles.md](generated/icon-profiles.md), and all commands are in
the shared [icon pipeline](icon-pipeline.md). This page adds only the
container-specific request contract.

## Container constraints

- Declare `"iconType": "container"` and the exact `containerSlot` metadata in
  editable JSON.
- Choose the accepted sub-profile keyshape before creating the filled preview.
- Keep the full centered 32×32 slot clear of container paint, including the
  centered stroke. The accepted keyshape does not shrink this protected square.
- Keep the empty outer icon recognizable; put identity-bearing detail in the
  available outer margin.
- Ship the empty container only.
- Also produce a non-shipping filled preview with an independently authored sub
  icon placed in the slot without scaling.
- Validate the empty container structurally and inspect the combined preview at
  true ship size for spacing and recognition.

Do not shrink the slot, move it off center, or scale the inserted sub icon to
make a crowded composition pass. Repair the editable container or simplify the
sub icon instead.

## Request to send

```text
Follow the repository's canonical icon pipeline and generate container icons
for:
- <container subject>
- <another subject, optional>

Accepted sub-icon keyshape: <sub-profile token, or choose per subject>
Output folder: <path, or omit to use generated/container-icons>

For each subject, deliver editable atomic JSON with iconType "container", the
empty design and ship SVG pair, complete QA evidence, and a non-shipping filled
preview using an accepted sub icon. Process only the listed subjects.
```

For one subject:

```text
Follow the canonical icon pipeline and generate a container icon of <subject>.
Choose the accepted sub-icon keyshape that best preserves the container's
identity. Deliver editable atomic JSON, both empty profile sizes, QA evidence,
and a non-shipping filled preview.
```

If this file is sent outside the repository, include `icon-pipeline.md`,
`icon-types.md`, `icon-rules.md`, `atomic-shapes.md`, and the generated profile
reference so links and machine-defined values remain available.
