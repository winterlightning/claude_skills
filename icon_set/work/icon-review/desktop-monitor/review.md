# Cloud monitor upload — main source review

- Side pair: `0005e7b2-b6eb-47bb-9b2c-8d04c5b409tr` (`cloud monitor upload`)
- Main source: `0005e7b2-b6eb-47bb-9376-770c2522288d` (`Monitor with Upward Arrow`)
- Existing reusable component: `container/desktop-monitor`
- Existing SVG SHA-256: `9c826bf38e2d1855d29b34be9506d1e7d643f76d5bbfaf5518b039f23e68217a`
- Discarded duplicate: `solo/desktop-monitor-solo-0005e7b2`
- Discarded SVG SHA-256: `70112ed0f555e78d3fe7bc1d8b9d50ef3516d466733c19c997b44bc2bb776ea2`

## Finding

The source depicts a monitor container hosting an upward arrow. The saved user-facing
classification correctly splits it into an empty monitor container plus an independent
up-arrow sub component, and explicitly says to reuse `container/desktop-monitor` rather
than generate a near-duplicate.

The later `desktop-monitor-solo-0005e7b2` candidate excluded the arrow and recreated the
same empty monitor as a SOLO48 icon. It passed numeric model QA, but `fidelity-review`
discarded it on 2026-09-21. That rejection is consistent with the saved classification:
the drawing was a duplicate in the wrong family, not a geometry failure.

## Visual assessment

- Intended complete source: monitor with an upward upload arrow.
- Existing component reading: a clear empty desktop monitor.
- Concept match: convincing for the monitor component; incomplete by itself for upload,
  which is expected because the arrow is an independent component.
- Keyshape/profile: keep the existing CONTAINER64 square construction. It provides the
  empty content area required to host the arrow.
- Symmetry: whole-object vertical mirror about `x = 32` for the CONTAINER64 monitor.
  The enclosure, stem and foot visibly support that structure.
- Numeric QA: pass for the existing container; the discarded solo also passed automatic
  QA, confirming that rejection was about routing/reuse rather than malformed geometry.
- Verdict: keep `container/desktop-monitor`; do not restore the discarded solo duplicate.

## Catalog issue

The current combination catalog still reports the main reference as `generated: []` and
the primitives catalog calls it unmatched. The side queue therefore presents it as a new
main icon even though the review database says to reuse `container/desktop-monitor`.
The missing piece is catalog attribution/remapping for the reviewed component decision,
not new monitor artwork. The up-arrow component must also be linked or generated before
the nested monitor-upload composition can be considered fulfilled.

## Authoring handoff

No new monitor should be authored. Reconcile the main source UUID with
`container/desktop-monitor`, then audit/link a suitable SUB32 upward arrow. If no suitable
arrow exists, author only that arrow with `$icon-sub`, preserving the monitor as the
existing CONTAINER64 component.
