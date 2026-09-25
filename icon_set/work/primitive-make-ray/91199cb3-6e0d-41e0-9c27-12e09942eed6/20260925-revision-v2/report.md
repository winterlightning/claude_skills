# Monitor

Circled-check monitor retained; user accepts its nested ring/screen and ring/check spacing as an exception.

- Source: `pictographic-primitives/other/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg`
- Source UUID: `91199cb3-6e0d-41e0-9c27-12e09942eed6`
- Keyshape: `SQUARE`
- Automatic full QA: `fail`
- Acceptance: `user-approved-exception`
- Reviewed at48px and192px, in light and dark themes.

Exception scopes: screen/status-ring clearance, status-ring/check clearance. The approval is bound to this exact SVG hash; the standard validator result is not altered.

## Findings

- mic [screen]: screen and status-ring are 5 apart on centerlines nearest (24, 6)<->(24, 11); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [status-ring]: status-ring and check are 5.394 apart on centerlines nearest (31.5214, 15.0585)<->(27, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
