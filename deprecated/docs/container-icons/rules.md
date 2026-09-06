# Container icon rules

Use `container` for an independently recognizable outer icon with a protected
centered region for a separately authored sub icon. This page owns container
composition and delivery policy. Apply the
[shared visual rules](../shared/icon-rules.md) for geometry, paint, spacing,
connections, naming, and negative space; use [profile.md](profile.md) for the
generated canvas, stroke, center, keyshape, and slot values.

## Empty container

- Declare `"iconType": "container"` and author directly on its configured native
  canvas and stroke (built-in defaults 64×64px and 4px). Export and review at
  that same size without a half-size derivative. Select a container keyshape and declare `keyfitCheck.targetToken`.
- Include the exact `containerSlot` coordinates and dimensions from the
  generated profile. Choose its `acceptedKeyshape` from the compatible sub
  profile before creating the filled preview.
- Keep the full configured centered slot clear of all container paint (built-in
  default 32×32), including the
  centered stroke. The accepted sub keyshape does not reduce this protected
  square.
- Keep the empty outer icon recognizable, placing identity-bearing detail in
  the available outer margin. Its paint must reach and remain inside the
  selected outer keyshape.
- Prefer one to three identity-bearing features,
  using a few large, legible shapes. Treat these as composition preferences;
  preserve the slot and the outer icon's recognition when simplifying.

## Filled preview

Author and review both the empty production icon and a non-shipping filled
preview containing a representative accepted sub icon.

- Author the sub independently using the [sub rules](../sub-icons/rules.md).
- Translate the sub into the declared slot without scaling. Keep the two
  editable sources separate and compose the preview through the shared
  pipeline's manifest-based preview command.
- Validate the empty container structurally, including the full protected
  region. Inspect the combined preview at the configured native container size for
  spacing and recognition.
- If the preview is crowded, simplify or recompose the container or sub icon.
  Do not shrink the slot, move it off center, or scale the inserted sub.

Ship the empty container only. Slot guides and the filled preview are review
artifacts and never become paint in the production container SVG.

### Preview manifest

Keep the manifest outside the editable-source folder. For example, save
`work/<job>/filled-preview.json` with:

```json
{
  "schemaVersion": 1,
  "kind": "container-filled-preview",
  "name": "key-container-filled-preview",
  "container": "editable/key-container.json",
  "sub": "editable/key-sub.json"
}
```

The `container` and `sub` paths must be relative JSON paths resolved from the
manifest's directory, not the shell's working directory. The sources must
declare `iconType` as `container` and `sub`, respectively, and the container's
`containerSlot.acceptedKeyshape` must match the sub's `keyfitCheck.targetToken`.
The compositor also checks the sub's painted keyshape containment before
placing it in the slot.

Use a distinct preview name and write the container-native preview SVG under
`work/<job>/qa/previews` with the
[shared preview command](../shared/icon-pipeline.md#5-emit-canonical-outputs).
Keep those files separate from production exports.

## Updating older assets

A legacy source whose canvas, stroke, keyshape, or slot no longer matches the
configured profile is stale. When migration is requested, recompose the outer
geometry on the current canvas, select a current keyshape, update slot metadata,
and re-emit the native SVG and any same-size compatibility alias. Globally scaling or merely translating old flattened artwork does not
create the usable space required around the sub icon.

## Delivery

Use a kebab-case name, appending `-container` when mixed-type output names could
collide. Deliver schema-version-2 editable JSON with slot metadata, the empty
configured-native SVG, the separate preview at the same container dimensions, and the evidence required by the
[shared pipeline](../shared/icon-pipeline.md).
