# Naming

**icon_id:** kebab-case matching `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`. Name the concept, not the drawing (`chevron-right`, not `angle-bracket`). Synonyms go in `aliases`, search terms in `keywords`. Follow an existing prefix family (`arrow-*`, `chevron-*`, `container-*`).

**Supplied `sym-<id>`:** keep it complete at the front, leading zeroes included, underscore converted to hyphen: `sym_000123` + Bell -> `sym-000123-bell`. Never invent one. Manifest output paths stay as given.

**Source metadata, every module:**
- `SOURCE_ICON_ID`: the full UUID from the source filename or the explicit ID in the brief, exactly. Size suffixes (`@48`) are not part of it. `None` only if none was supplied.
- `SOURCE_PATH`: the supplied path, or `None`.
- `AUTHOR`: your own model, lowercase-hyphenated. Never `None`, never a generic label, never the model you are imitating. Ask if unsure. `astra-chatgpt` = everything before the field existed. Patching a module makes `AUTHOR` yours. Say in your reply if you introduced a new value.

**Filename:** with a source ID, `<descriptive_name>_<source_id_with_underscores>.py`, ID once. Without, `<icon_id_with_underscores>.py`. Before creating, search the family folder for the ID in both hyphen and underscore forms and patch the match instead. Ambiguous matches: resolve before editing.

**Family suffixes:** identity is `(icon_id, profile)`. The same concept in another family gets a suffix on the same base (`bell`, `bell-sub`, `bell-container`), each separately drawn. No suffix for a single-family icon.

**Variants:** `-variant-N` is reserved, not implemented. If asked for alternatives, render, keep the stronger, report the rest. Review revisions use `create_variant.py`, which produces `-v2` style ids.

**Element ids:** name parts for what they are (`shaft`, `bar-top`, `ring-inner`).
