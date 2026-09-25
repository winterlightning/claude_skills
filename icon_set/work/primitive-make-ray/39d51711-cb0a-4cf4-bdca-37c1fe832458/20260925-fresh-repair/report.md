# private-message-bubble

Full PM text sits in a rounded speech bubble with an integral lower-left tail. M retains slanted outer strokes from the reference.

- Source UUID: `39d51711-cb0a-4cf4-bdca-37c1fe832458`
- Reference: `pictographic-primitives/other/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg`
- Author: `gpt-6`
- Keyshape: `HRECT_L`; visible ink bounds `[2, 6, 46, 42]`. Wide envelope preserves horizontal text and its enclosure.
- Full QA: **fail**.

## Construction and omissions

Lucide message-square original and atomic-debug: rounded enclosure and integrated tail; supplied reference governs PM.

No defining component omitted.

## Visual review

Both themes/native48: PM remains legible. Bubble is squarer than the oval source; narrow M valleys and P bowl remain too tight. No visual approval for release.

## Validation

- mic [bubble]: bubble and m are 6.99947 apart on centerlines nearest (43.9989, 28.0859)<->(37, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [bubble]: bubble and p-stem are 7.9994 apart on centerlines nearest (7.972, 9.08874)<->(12, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- internal-spacing [p-stem / p-bow]: p-stem-2 and p-bow-1 have 3.5224 units of ink clearance over 4.1881 units; requires 4; review required
- internal-spacing [m]: m-1 and m-3 have 0.3918 units of ink clearance over 6.5911 units; requires 4; review required
- internal-spacing [m]: m-1 and m-4 have 2.4418 units of ink clearance over 4.9655 units; requires 4; review required
- internal-spacing [m]: m-2 and m-4 have 0.3918 units of ink clearance over 6.5911 units; requires 4; review required
