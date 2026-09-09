# Reference combination gate

Before authoring a referenced primitive, visually inspect the reference and
classify it as standalone, container combination, or side combination. Use the
`icon-making` skill in the repository skill folders as the routing entry point.

A container combination is an independently meaningful enclosure hosting a
separate icon. A side combination is a main noun/enclosure with a separate
modifier beside it. Neither should become one new primitive. Reject the
combined candidate and prepare exactly two standalone component briefs:
container + sub, or solo/container + sub respectively. The family decision for
each component is made by `icon-making` and passed to its authoring skill.

Do not split intrinsic features of one object (a teapot handle, a lid, a face,
a screen's structural controls) into separate icons. Geometry alone is not
proof of combination; both subjects must be independently meaningful.

Use the review app's Reject action for a built icon. Before generation, write
a component JSON handoff and run `icon_set/scripts/queue_brief.py` as described
in the `icon-making` skill. Keep source paths/UUIDs, a clear reason, and exactly
two names/families/descriptions. Never delete the rejected icon or its exports.
When the task is already a component Pending brief, isolate its specified
component and proceed; do not repeatedly reject the full reference.
