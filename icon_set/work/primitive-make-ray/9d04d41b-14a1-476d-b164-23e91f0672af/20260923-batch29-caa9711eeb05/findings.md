# A location-message bubble overlaps a smartphone.

SQUARE, (4, 4, 44, 44): Balanced complete composition uses the square envelope.

Construction: One coherent phone enclosure; source message overlap retained.

References: ['icon_set/references/lucide/original/smartphone.svg', 'icon_set/references/lucide/atomic-debug/smartphone.svg']

Omissions/reductions: Small home-button tick and phone divider omitted because they crowd the overlapping message bubble.

Native and enlarged light/dark review: Smartphone, message tail and location pin are all retained. Pin is crowded against bubble boundary and merges visually. MIC fails; not approved.

```text
status: invalid
  ERROR  mic [bubble]: bubble and pin are 2 apart on centerlines nearest (29, 30)<->(29, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
