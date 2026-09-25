# Sedan car

Lowered the cabin, smoothed hood and trunk into a continuous body, and reattached body and sill to wheel sides. Natural car ink bounds(2,10)-(46,38) deliberately relax the standard HRECT_M height by2 at each edge.

- Source: `pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg`
- Source UUID: `796e3289-99b8-4ef8-bce0-4e8fa2bfefc8`
- Keyshape: `HRECT_M`
- Automatic full QA: `fail`
- Acceptance: `user-approved-exception`
- Reviewed at48px and192px, in light and dark themes.

Exception scopes: keyshape vertical fit, body/wheel internal spacing. The approval is bound to this exact SVG hash; the standard validator result is not altered.

## Findings

- canvas/keyshape bounds: visible ink (2, 10, 46, 38) does not match the HRECT_M envelope (2, 8, 46, 40) (deltas [0.0, 2.0, 0.0, 2.0], tolerance 0.0)
- internal-spacing [body / wheel-13]: body-3 and wheel-13-0 have 2.9533 units of ink clearance over 5.6543 units; requires 4; review required
- internal-spacing [body / wheel-35]: body-10 and wheel-35-1 have 2.0695 units of ink clearance over 2.2087 units; requires 4; review required
- internal-spacing [body / wheel-35]: body-11 and wheel-35-1 have 2.2202 units of ink clearance over 5.1048 units; requires 4; review required
