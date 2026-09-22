# Reference triage

An empty enclosure is a standalone **solo** subject when no separate icon is
hosted inside: this includes boards, screens with keyboards, speech bubbles,
and overlapping empty frames. Enclosing geometry, a structural clamp/stand, or
a saved `container` family label does not make a container combination. Reserve
container routing for the wrapper component of an actual hosted-icon combination
or an explicit container-component request. Follow the current user's family
correction over an older saved label; never invent an inner icon to justify a split.

Before authoring a referenced primitive, look at the render and classify it: **standalone**, **container combination** (a meaningful main wrapper with a separate sub icon centered inside) or **side combination** (a main subject plus a separate reusable sub icon on its side or corner). Combinations are never one primitive. In `icon-solo-distilled`, classify the source in the gallery and defer it: `status: "skip", reason: "container"` for container combinations; `status: "skip", reason: "combination"` for side combinations. Save both `main_brief` and `sub_brief` on the source UUID through `/api/primitives/status`, and update the saved reference family/brief through `/api/primitives/briefs` (container main: `container`; side main: `solo` or `container`; sub: `sub`). Preserve useful editorial content and describe each component independently, including exclusions and later placement. Verify both records by reading them back. Do not generate either component during that solo run. See `icon-solo-distilled` for the persistence payload and incomplete-save handling. In an explicitly requested component-preparation task, prepare two component briefs (container + sub, or solo/container + sub). `icon-making` assigns the families. Text components are typeface reuse, not new primitives.

Do not split intrinsic parts (teapot handle, lid, face, clock hands, screen controls). Geometry alone is not proof; both halves must be independently meaningful, and for a side split the second must be a modifier of the first.

**Side-combination test, all must hold:**
- Main subject still reads with the candidate removed.
- The second element is a reusable action or state glyph (check, plus, cross, warning, lock, arrow), not a physical part, held object, companion or scene detail.
- Placement reads as a badge: any corner, beside, above or below; may overlap or sit in a cleared gap.

| Reference | Reading |
|---|---|
| Cloud with corner check; person with plus badge | Side combination |
| Cup and saucer; mortar and pestle; person holding a tool | Standalone, parts belong together |
| Two people; fruit cluster; sun behind cloud | Standalone group or scene |
| Padlock on a door hasp vs lock badge floating over a folder | Physical relationship vs side modifier |

If both readings stay plausible, mark uncertain and record both; do not force a split. In `icon-brief`, save briefs for clear side combinations without waiting; always save a later-generation brief for a SKIP. Briefs do not authorize generation.

For a built icon use the review app's Reject. For an explicitly requested component-preparation task, write a component JSON handoff and run `icon_set/scripts/queue_brief.py` (see `icon-making`), keeping source paths, UUIDs, reason and two names/families/descriptions. Never delete the rejected icon. A Pending component brief already names its component: isolate it and proceed.
