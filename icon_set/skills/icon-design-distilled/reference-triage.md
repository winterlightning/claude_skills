# Reference triage

Before authoring a referenced primitive, look at the render and classify it: **standalone**, **container combination** (a meaningful enclosure hosting a separate icon) or **side combination** (a main subject plus a separate modifier beside it). Combinations are never one primitive: reject and prepare exactly two component briefs (container + sub, or solo/container + sub). `icon-making` assigns the families. Text components are typeface reuse, not new primitives.

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

For a built icon use the review app's Reject. Before generation, write a component JSON handoff and run `icon_set/scripts/queue_brief.py` (see `icon-making`), keeping source paths, UUIDs, reason and two names/families/descriptions. Never delete the rejected icon. A Pending component brief already names its component: isolate it and proceed.
