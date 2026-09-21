# Symbol family

A **symbol** is the small drawing hosted inside a container. A **sub** icon sits beside a main subject. These are separate families with independent editable models, even when their initial artwork is identical.

- Family: `symbol`; profile: `SYMBOL32`; base: `Symbol32` from `icon_set.model.icons.symbol._base`.
- Models: `icon_set/model/icons/symbol/`; validated exports: `published/symbol32/`.
- Native canvas 32×32; integer grid 1; stroke 4; round caps and joins; MIC 2. SYMBOL32 copies the SUB32 numeric rules exactly. Use the profile/keyshape contracts, without changing tolerances.
- Existing natural-width text symbols use `TextSymbol32` from `symbol._text_base`. Preserve their existing text layout specialization.
- Follow `symbol-construction.md`, `authoring.md`, and `human-reference.md` for human forms. Read the existing Python model before a repair.
- For a repair, create an independent same-family variant with `create_variant.py --family symbol`. Never edit its linked side counterpart as a side effect.
- Preserve source IDs, source paths and author metadata. Cross-family counterparts are `related_role_icons` / `related_group` links, not `variant_of` ancestry.
- Validate the model and run `inspect_icon` from `icon_set.validation.library_qa`. A geometry or review failure must remain visible. Preview at native size in both themes.
- All 32/24 placement decisions belong to the composition review. Do not distort a container or silently scale final symbol geometry to force a fit.
