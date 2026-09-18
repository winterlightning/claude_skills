# Side-combination sub reference generation

24 source-linked outputs published: 11 repaired SOLO48 icons and 13 existing-typeface TEXT32 layouts. All were reviewed at native size in light and dark themes. Original source IDs and paths are preserved. AUTHOR: gpt-6.

## Validation

- Targeted solo family build: exit 0; all 11 models pass validation with zero warnings and release QA.
- Text: existing preferred glyphs only, ink height 32, natural variable width, uniform glyph proportions, effective stroke 4, no clipped ink.
- Focused Python checks: 24 passed. Typeface JavaScript test: passed.
- Full unittest discovery was attempted, encountered disk-space errors in gallery staging, and was interrupted. It is not a full-suite pass. The initial gallery build also hit disk exhaustion; the serial retry succeeded after temporary test storage was released.
- All 24 outputs are present in the gallery, with emitted solo SVGs checked against the current models.

## Solo drawings

| Reference | Drawing | Construction and reduction |
|---|---|---|
| 19 | Hand Pointing at 3D Cube | SQUARE keeps the cube above-right of a pointing hand; shortened palm and finger detail to preserve clearance. Lucide hand informed continuous contours. Intentional upper-right cube placement. |
| 29 | Mechanical Robotic Hand | HRECT_L retains the horizontal mechanical palm and raised digit. Lucide hand informed the silhouette; reduced mechanical panel detail. Intentional right-pointing digit. |
| 31 | Minimalist Pig Face | SQUARE frames a symmetric pig face. Lucide piggy-bank informed the snout/ear vocabulary; omitted nostrils at native size. |
| 33 | Shipping Delivery Truck | HRECT_L follows a delivery truck silhouette. Lucide truck informed the joined cargo/cab shape. Small complete circular wheels use the existing approved hole exception; no wheel spokes. |
| 34 | Simple Bicycle | SQUARE allows an elevated bicycle frame and equal wheels. Lucide bike informed equal circular wheels; lowered frame tubes and spokes omitted for open negative space. |
| 35 | Simple Bicycle Icon | Same bicycle subject reconstructed on SQUARE, with its own source identity preserved. |
| 36 | Simple Circular World Globe | CIRCLE matches the round globe. Lucide globe informed the structural meridian/equator. Replaced two crowded latitudes with one equator. |
| 44 | Three Lightning Bolts | HRECT_L holds three repeated open bolts. Lucide zap informed angular lightning construction; shared repeat spacing and unequal slopes preserve clear gaps. |
| 48 | Two Wheeled Pedal Bicycle | Same bicycle subject reconstructed on SQUARE, with its own source identity preserved. |
| 50 | Vintage Movie Camera | SQUARE retains two film reels and camera/lens silhouette. Lucide video informed the joined body/lens; two equal reels have clear separation. Intentional right-facing lens. |
| 51 | Wallet with Cash Bill | SQUARE retains a wallet, protruding bill and right clasp. Lucide wallet informed the clasp and body. Straightened the bill edge to remove the narrow wedge. |

## Typeface labels

| Text | Canvas width | Ink height |
|---|---:|---:|
| 3DS | 74.497 | 32 |
| A3 | 50.318 | 32 |
| API | 68.146 | 32 |
| AI | 41.471 | 32 |
| C++ | 77.192 | 32 |
| CCPA | 100.565 | 32 |
| DMG | 84.573 | 32 |
| FAKE | 100.266 | 32 |
| C5 | 47.911 | 32 |
| X2 | 50.976 | 32 |
| UV | 52.365 | 32 |
| XLSX | 100.881 | 32 |
| 0% | 50.110 | 32 |


## Remaining work

- Reference 45, Three Star Rating Symbol: original small outlines pass the model envelope but fail release QA with 3 undersized holes and internal spacing warnings. Enlarged outlines fail MIC between top/left, top/right (6.40312 centerline units) and left/right (4 units), below the required 8. The original module is preserved; the larger attempt is saved as `three-star-attempt.py`. No thresholds were changed and no exception was claimed.
- 28 framed/composed references were split into 56 standalone component handoffs under `pending-components/`, with source JSON under `component-handoffs/`. These are saved handoffs, not new drawings or database-queued approvals. Text within these compositions is marked for existing-glyph reuse.

The icon-solo skill requires: “Before reduction, apply ... reference-triage.md” and directs combined references to component briefs. Its release rule says “If something could not be made to pass, name the check and the element and stop”. Those rules explain the remaining composition work and the three-star blocker.

28 of the original 53 source references are still ungenerated.

Text correction: all 13 emitted SVGs independently measured at 32 units of painted ink height (including stroke). Gallery text integration tests: 3 passed.
