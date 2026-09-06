# Sub-icon rules

Use `sub` for a compact independent symbol that may also be inserted into a
container. This page owns sub-specific composition and delivery policy. Apply
the [shared visual rules](../shared/icon-rules.md) for geometry, paint,
connections, naming, and negative space; use [profile.md](profile.md) for the
generated canvas, stroke, center, keyshape, and distance values.

## Composition

- Declare `"iconType": "sub"` in every editable source and author directly on
  its configured native canvas and stroke (built-in defaults 32×32px and 4px).
  Export and review at that same size without a half-size derivative. Recompose
  the subject for that canvas; never
  make a sub icon by scaling a finished normal icon.
- Prefer one dominant silhouette and no more than two identity-bearing internal
  features. Favor recognition at the sub native size when choosing details; do
  not impose a count of geometry elements.
- Select a sub keyshape from the dominant whole-icon silhouette and declare
  `keyfitCheck.targetToken` explicitly. In the built-in defaults the sub circle
  and square share full-canvas bounds; a bounding box alone cannot distinguish
  them. Always use the configured token's actual shape and dimensions.
  The agent may approve a subject- or prototype-justified
  [keyshape exception](../shared/icon-pipeline.md#keyshape-exceptions) using
  optical mode; containment, native-size review, and all three gates still apply.
- Keep the centered stroke inside the canvas even where paint reaches its edge.
  Viewport clipping does not count as a keyshape fit.
- Use the sub profile's configured minimum distinct centerline distance
  (built-in default 3u).
  Shared R5's visual-opening and connection requirements still apply where
  relevant.
- Inspect recognition and negative space at the exact sub native size in the
  generated profile.

A sub icon is independently recognizable. A composite corner badge follows the
[normal badge policy](../icons/rules.md#composite-corner-badges), not this profile.
When pairing a sub icon with a container, retain the independently authored sub
source and place it in the compatible slot without scaling.

With the built-in 4u stroke and 3u centerline floor, centerlines can have
paint envelopes overlapping by up to 1u. This compact spacing allowance does not
satisfy a declared visual opening; use shared R5's painted clearance for those.

## Updating older assets

Recompose and re-emit an older sub asset for its selected current token instead
of merely renaming its metadata. Use the shared core pipeline for new work;
`output_subicon/build-sub-icons.py` is a historical helper for reproducing old
examples.

## Delivery

Use a kebab-case name, appending `-sub` when mixed-type output names could
collide. Deliver schema-version-2 editable JSON, the configured native SVG, and the
evidence required by the [shared pipeline](../shared/icon-pipeline.md). Review
the sub on its own even when it is also included in a container preview.
