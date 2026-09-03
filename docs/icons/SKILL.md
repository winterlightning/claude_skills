---
name: icons
description: Create, edit, or rework complete standalone Unlimited Shapes main icons using the normal profile, including composite corner badges. Use the sub-icons or container-icons skill for those separate profiles.
---

# Normal icons

This is the `normal` role/workflow template. Resolve its canvas, stroke,
keyshapes, and validation settings from `core/icon_profiles.json`; the built-in
default is 48×48px with 4px stroke, not an immutable size. Author, export,
and review at that resolved native size, 1u = 1px, without half-size derivatives.
The canonical SVG is `<name>.svg`.

For profile changes or a custom named type, use the
[profile configuration guide](../shared/profile-configuration.md). Custom types
follow the generic shared pipeline with their resolved JSON profile; choose
role-specific guidance only when it fits the requested use.

Read [rules.md](rules.md) and the generated [profile.md](profile.md), then apply
the [shared visual rules](../shared/icon-rules.md). These files define the normal
type; exact profile geometry comes from `core/icon_profiles.json`.

Follow the [shared pipeline](../shared/icon-pipeline.md). Load only the adapter
that matches the input:

- One supplied SVG: [single-icon adapter](../shared/icon-execution-steps.md).
- An explicitly selected SVG set: [batch adapter](../shared/icon-batch-execution-steps.md).
- A symbol-library `kind: "rework"` payload: [rework adapter](rework.md).
- A local manifest-based rework pack: [local pack lane](rework.md#local-manifest-pack-lane).
- A subject description without an SVG: use the shared pipeline's brief-only
  intake.

Use the [geometry and reference guide](../shared/atomic-shapes.md) for schema-version-2
elements and relevant Lucide original/debug pairs. New contours need no registry
change. Consult the [script inventory](../shared/scripts.md) for command contracts.
Open specialist QA guides only when the relevant gate needs interpretation or
repair.

Run commands from the repository root. Use the requested work folder, or
`work/<job>` when none is supplied. Keep source evidence, editable JSON, output,
and QA separate according to the shared pipeline.

Deliver the editable source, configured native SVG, and the pipeline's required
QA evidence. Do not upload without explicit authorization. Use [request.md](request.md)
when preparing a portable request.
