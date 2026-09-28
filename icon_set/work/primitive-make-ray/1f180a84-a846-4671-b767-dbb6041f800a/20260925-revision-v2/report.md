# Passport

Passport changed from SQUARE to VRECT_L, with a taller cover and globe radius11 instead of10. Both curved meridians and equator are restored. Cover/globe spacing is retained as an approved exception.

- Source: `pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg`
- Source UUID: `1f180a84-a846-4671-b767-dbb6041f800a`
- Keyshape: `VRECT_L`
- Automatic full QA: `fail`
- Acceptance: `user-approved-exception`
- Reviewed at48px and192px, in light and dark themes.

Exception scopes: globe/cover clearance. The approval is bound to this exact SVG hash; the standard validator result is not altered.

## Findings

- mic [cover]: cover and globe are 5 apart on centerlines nearest (8, 25)<->(13, 25); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
