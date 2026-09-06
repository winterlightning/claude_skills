---
name: sub-icons
description: Create or edit standalone Unlimited Shapes sub icons, including sub icons inserted into containers. Use this for the sub profile, not composite corner badges or outer containers.
---

# Sub icons

This is the `sub` role/workflow template. Resolve its canvas, stroke,
keyshapes, and validation settings from `core/icon_profiles.json`; the built-in
default is 32×32px with 4px stroke, not an immutable size. Author, export,
and review at that resolved native size, 1u = 1px, without half-size derivatives.
The canonical SVG is `<name>.svg`.

For profile changes or a custom named type, use the
[profile configuration guide](../shared/profile-configuration.md). Custom types
follow the generic shared pipeline with their resolved JSON profile; choose
role-specific guidance only when it fits the requested use.

Read [rules.md](rules.md) and the generated [profile.md](profile.md), then apply
the [shared visual rules](../shared/icon-rules.md). These files define the sub
type; exact profile geometry comes from `core/icon_profiles.json`.

Follow the [shared pipeline](../shared/icon-pipeline.md) for both input modes:
**concept name + minimal description**, without references or with optional
SVG/PNG/other reference files. Analyze the input and intended role first, read
the selected JSON profile, then plan and author the icon. A text-only brief needs
no fabricated source SVG or detector run; inspect non-SVG references appropriately.
Load only the adapter that matches actual supplied inputs:

- One supplied SVG: [single-icon adapter](../shared/icon-execution-steps.md).
- An explicitly selected SVG set: [batch adapter](../shared/icon-batch-execution-steps.md).
- Name + description without references: use shared brief-only intake.
- Name + description with PNG/other files: use shared reference-backed intake.

After emission and structural/grid/overlap prerequisites, require **distance →
holes/pinches → canvas/keyshape**, in that order, for this profile. Read failing
pairs/zones/bounds, repair editable geometry, regenerate both aliases, and restart
at distance. Deliver only fresh passes from all three on the same SVG/profile,
plus native-size visual approval. Unresolved reviews, checker errors, missing or
stale results block completion; never weaken the profile to force a pass.

When exact keyshape proportions would distort the subject, the AI may approve
a [keyshape exception](../shared/icon-pipeline.md#keyshape-exceptions) without
additional user approval. Record the rationale and measured painted bounds in
optical mode, rerun all gates, and label the passing result as an exception.
Only approve exceptions whose measured centerline width and height are each
divisible by 4; record that size in the rationale and reject non-multiples
even if the optical checker passes.
This does not waive containment, distance, holes, or native-size visual review.

Use the [geometry and reference guide](../shared/atomic-shapes.md) for schema-version-2
elements and relevant Lucide original/debug pairs. New contours need no registry
change. Consult the [script inventory](../shared/scripts.md) for command contracts.
Open specialist QA guides only when the relevant gate needs interpretation or
repair. If the request also includes the outer container, use the separate
[container skill](../container-icons/SKILL.md) for that source and its preview.

Run commands from the repository root. Use the requested work folder, or
`work/<job>` when none is supplied. Keep source evidence, editable JSON, output,
and QA separate according to the shared pipeline.

Deliver the editable source, configured native SVG, and the pipeline's required
QA evidence. Do not upload without explicit authorization. Use [request.md](request.md) when preparing a portable request.
