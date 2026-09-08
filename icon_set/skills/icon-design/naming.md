# Naming

## Concept ids

Lower kebab-case: `heart`, `chevron-right`, `arrow-up-left`, `container-circle`.
The schema enforces `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`.

Name the **concept**, not the drawing. `chevron-right` points right; it is not
`angle-bracket`. Synonyms belong in `aliases`, not in a second icon:

```python
class ChevronRight(Sub32):
    icon_id = "chevron-right"
    aliases = ("caret-right", "forward", "disclosure")
    keywords = ("right", "next", "forward", "more")
```

`aliases` are other names for the same thing. `keywords` are search terms. Both
feed discovery, so an icon nobody can find is an icon nobody uses.

Family prefixes group related concepts and sort together: `arrow-*`,
`chevron-*`, `triangle-*`, `container-*`. Follow an existing family when the new
icon belongs to one.

## Supplied symbol ids

When the source or its metadata carries a `sym-<id>` or `sym_<id>` identity,
**keep it at the front of the name**, complete, including leading zeroes.
Convert the underscore to a hyphen in generated names only.

```
sym_000123  +  subject "Bell"   ->  sym-000123-bell
```

Do not add a prefix that is already there, do not truncate the id, and do not
rename a delivery path to match. Where a manifest names an output file, that
path stays exactly as the manifest gives it, even when it differs from the icon
name.

If no symbol id was supplied, use ordinary descriptive naming. Do not invent
one. If two supplied ids conflict, resolve that with the user before authoring.

## Reference ids in Python scripts

Every generated Python icon module or one-off icon generation script must retain
the supplied reference icon's ID, even when the brief also supplies a descriptive
name or proposed `icon_id`. Extract a UUID from the source filename (the complete
trailing UUID, not just its last segment), or use the explicit source ID in the
brief/metadata. Preserve it exactly in module-level `SOURCE_ICON_ID`, and store
the supplied source path in `SOURCE_PATH`. A PNG render and its `@64`/`@48`/`@32`
copy refer to the same source ID; the size suffix is not part of that ID.

For new Python files, use `<descriptive_name>_<source_id>.py`, replacing hyphens
with underscores for a Python-safe filename. Include the ID only once. Keep the
descriptive registry `icon_id` and the source identity separate; existing
`sym-<id>` naming rules still apply.

For example, source
`container_icons/svg/blank-document-clipboard-200fc64a-3a4a-41c0-b9a5-1b38a7eada67.svg`
produces `blank_document_clipboard_200fc64a_3a4a_41c0_b9a5_1b38a7eada67.py` with:

```python
SOURCE_ICON_ID = "200fc64a-3a4a-41c0-b9a5-1b38a7eada67"
SOURCE_PATH = "container_icons/svg/blank-document-clipboard-200fc64a-3a4a-41c0-b9a5-1b38a7eada67.svg"
```

Before creating a module, search existing Python files for the exact source ID
and its underscore form. Patch the matching module for the requested family
instead of creating another file under a new name. Preserve existing module
paths when patching and add missing source metadata. If multiple matches remain
ambiguous, resolve the target before editing. If no source ID was supplied, do
not invent one: use the descriptive filename, `SOURCE_ICON_ID = None`, and the
source path if available (`None` otherwise).

## Family suffixes

Identity is `(icon_id, profile)`, and the profile is the family's, so one id
names one drawing in one family. A concept genuinely wanted in more than one
family distinguishes them with a suffix on the same base — `bell` (the solo
subject at 48), `bell-sub` (the 32 glyph), `bell-container` (the 64 enclosure).
Each is **separately authored geometry** in its own folder; a suffix never
means a scaled copy. Do not add a suffix to an icon that exists in one family
only.

## Variants: reserved, not implemented

The `-variant-N` suffix (`sym-000123-bell-variant-1`) is **reserved** for
alternative designs of one concept. This release does not implement a variant
axis: one drawing per `(icon_id, profile)`.

If asked for alternatives, render them for comparison, keep the stronger one,
and say what you set aside. Do not invent variant names to ship several — that
would encode an identity model that does not exist yet.

## Element ids

Inside an icon, name parts for what they are: `lobe-left-outer`, `shaft`,
`head`, `bar-top`, `ring-inner`. Every validator failure quotes the element id
back at you, so a descriptive one turns a message into a location.
