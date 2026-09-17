# Reference combination gate

Before authoring a referenced primitive, visually inspect the reference and
classify it as standalone, container combination, or side combination. Use the
`icon-making` skill in the repository skill folders as the routing entry point.

Text/number components follow [typeface.md](typeface.md): preserve their exact
content and reference existing typeface glyph IDs in a reuse/layout brief,
instead of generating new letter/number primitives. Apply this exception to
the component-authoring instructions below.

A container combination is an independently meaningful enclosure hosting a
separate icon. A side combination is a main noun/enclosure with a separate
modifier beside it. Neither should become one new primitive. Reject the
combined candidate and prepare exactly two standalone component briefs:
container + sub, or solo/container + sub respectively. The family decision for
each component is made by `icon-making` and passed to its authoring skill.

Do not split intrinsic features of one object (a teapot handle, a lid, a face,
a screen's structural controls) into separate icons. Geometry alone is not
proof of combination; both subjects must be independently meaningful. Even
independent meanings are insufficient for a side split: there must be a
main-subject-plus-modifier relationship, rather than a natural multi-object
subject or scene.

## Side-combination decision

Inspect the full render and ask whether all of these are supported:

- The main subject remains recognizable with the candidate modifier removed.
- The second element reads as a separate, reusable action/state glyph (such as
  a check, plus, cross, warning mark, lock, or action arrow) applied to that
  subject, rather than a physical part, held object, companion, or scene detail.
- Its placement supports a badge/modifier reading: commonly a smaller mark at
  bottom-left, but also bottom-right, either upper corner, beside, above, or
  below the main subject. It may overlap the outline or sit in a cleared gap.

Size, location, overlap, and the removal test are supporting evidence, not proof
by themselves. A small object in a corner is not automatically a modifier;
likewise, a badge need not have a circular border or be at bottom-left.

Examples to distinguish by their visible relationship:

| Reference | Reading |
|---|---|
| Cloud with a separate corner check; person with an adjacent plus badge | Side combination: subject plus status/action modifier |
| Cup and saucer; mortar and pestle; person holding a tool | Standalone subject: the objects belong together physically or functionally |
| Two people; a cluster of fruit; sun behind a cloud | Standalone group or scene, absent a separate modifier |
| Teapot handle; face; a clock's hands | Intrinsic parts, not separate modifiers |
| Padlock attached to a door hasp vs. floating lock badge over a folder | Physical object relationship vs. side modifier; inspect attachment and composition |

If either interpretation remains plausible after inspecting the individual
render, mark the reference uncertain and record both readings. Do not force a
split. During `icon-brief`, save independent briefs for clear side combinations
without waiting for human review. Preserve review evidence and unresolved
questions; if a source is marked SKIP, always save a later-generation brief.
Preparing briefs does not authorize queueing or generation.

Use the review app's Reject action for a built icon. Before generation, write
a component JSON handoff and run `icon_set/scripts/queue_brief.py` as described
in the `icon-making` skill. Keep source paths/UUIDs, a clear reason, and exactly
two names/families/descriptions. Never delete the rejected icon or its exports.
When the task is already a component Pending brief, isolate its specified
component and proceed; do not repeatedly reject the full reference.
