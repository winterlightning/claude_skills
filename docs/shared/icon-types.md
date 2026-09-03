# Choose an icon type

Choose the type before constructing geometry, selecting a keyshape, or setting proportions. Declare
`iconType` in editable JSON; do not infer it from finished bounds.

| Type | Purpose | Start here | Rules and profile |
| --- | --- | --- | --- |
| `normal` | Complete standalone icon, including a normal icon with a semantic corner badge | [Normal skill](../icons/SKILL.md) | [Rules](../icons/rules.md) · [Profile](../icons/profile.md) |
| `sub` | Compact standalone symbol that can also be inserted into a container | [Sub skill](../sub-icons/SKILL.md) | [Rules](../sub-icons/rules.md) · [Profile](../sub-icons/profile.md) |
| `container` | Recognizable outer icon with an empty centered slot for an accepted sub icon | [Container skill](../container-icons/SKILL.md) | [Rules](../container-icons/rules.md) · [Profile](../container-icons/profile.md) |

A request for an icon inside another icon normally needs separate container and
sub sources. A normal corner badge follows the normal-icon rules. Use the user's
intended role to choose; clarify only when that choice would change the subject
or requested behavior.

Each type's rules own its detail budget, additional constraints, and delivery
requirements. All types also use [shared rules](icon-rules.md) and the
[shared pipeline](icon-pipeline.md).

## Profile authority

[`core/icon_profiles.json`](../../core/icon_profiles.json) defines canvas, stroke,
center, keyshapes, distinct-part distance, inheritance, and container-slot values.
The local `profile.md` pages and [combined reference](icon-profiles.md) are
generated from that source. Code resolves it through
[`core/icon_profiles.py`](../../core/icon_profiles.py).

```bash
python3 core/generate_profile_assets.py
python3 core/generate_profile_assets.py --check
```

New sources always declare their type, profile canvas and stroke, and intended
`keyfitCheck.targetToken`. Omitted `iconType` means `normal` only for compatibility
with older editable sources. Recompose geometry on the chosen profile; changing
type metadata or scaling a flattened final SVG does not convert an icon.
