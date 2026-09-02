# Icon types

Choose `normal`, `sub`, or `container` before selecting atoms, a keyshape, or
proportions. The type is explicit editable metadata and is never inferred from
finished bounds.

The machine-readable authority for canvas, stroke, center, keyshape, distinct-part
distance, and container-slot values is
[`core/icon_profiles.json`](../core/icon_profiles.json).
[`generated/icon-profiles.md`](generated/icon-profiles.md) is regenerated from
that source with:

```bash
python3 core/generate_profile_assets.py
```

Do not hand-copy numeric profile tables into workflow documents. Use the
generated reference or load the profile in code through
`core/icon_profiles.py`.

| Type | Purpose |
| --- | --- |
| `normal` | Complete standalone icon. |
| `sub` | Simpler standalone icon that can also be inserted into a container. |
| `container` | Outer icon with a centered paint-free 32×32 slot for an accepted sub icon. |

All profiles author at their declared design size and emit at exact half scale.
A sub icon is recomposed on its own grid; it is never made by scaling a finished
normal icon.

## Editable metadata

Every source declares its type, profile canvas, Regular stroke, and keyshape:

```json
{
  "name": "example",
  "iconType": "normal",
  "canvas": 48,
  "strokeWidth": 4,
  "keyfitCheck": { "targetToken": "square-40" },
  "instances": []
}
```

`iconType` may be omitted only for backward-compatible normal sources. New
sources always declare it.

## Normal

Use the normal profile for a complete icon. Apply the shared rules in
[icon-rules.md](icon-rules.md), choose the keyshape from the normal profile,
and review the exact ship output.

## Sub

Use the sub profile for a compact independent symbol. Prefer one dominant
silhouette, 1–5 instances, and no more than two identity-bearing internal
features. Apply the shared grid, angle, and negative-space rules, but use the sub
profile's 3u minimum centerline distance for distinct parts instead of the normal
profile's 4u floor. Then review at the sub profile's true ship size.

## Container

A container uses its dedicated 64×64 design profile and emits a 32×32 ship
asset. Its unchanged 32×32 sub slot is centered inside that larger canvas, so
the outer artwork has real room around an independently authored sub icon. A
container declares the exact slot from the container profile:

```json
{
  "iconType": "container",
  "canvas": 64,
  "strokeWidth": 4,
  "containerSlot": {
    "x": 16,
    "y": 16,
    "w": 32,
    "h": 32,
    "acceptedKeyshape": "square-24"
  }
}
```

Container paint, including its centered stroke, must remain outside the entire
centered 32×32 slot. This guarantees the actual empty area can contain the full
sub design canvas. `acceptedKeyshape` still selects the compatible sub silhouette
for the filled preview, but it never reduces the protected square. Author and
review both:

1. The empty container, which must remain recognizable and reach its outer
   keyshape.
2. A non-shipping filled preview with a representative accepted sub icon placed
   in the slot without scaling.

If the preview is crowded, simplify the container or sub icon. Do not shrink
the slot, scale the inserted icon, or move it off center. Slot guides and the
preview never ship in the empty production SVG.

Legacy 48×48 container sources are not valid on the new profile. Recompose the
outer instances on the 64×64 canvas, select a container keyshape, update the
slot metadata, and re-emit both SVG sizes. Do not globally scale or merely
translate old flattened artwork; that creates padding without creating usable
space around the sub icon.

## Naming and delivery

Use kebab-case names. Append `-sub` or `-container` where mixed-type output
folders could otherwise collide. Deliver editable JSON plus the exact design
and ship SVGs. A container also includes its filled review preview and declared
slot metadata.
