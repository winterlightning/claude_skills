# Unclear meaning — 43 original icons repaired

All 43 live Disapproved icons whose latest feedback for the current revision was `meaning` were reviewed against their names and supplied source images. All 43 original Python models were changed in place, retaining their existing icon IDs, source IDs and filenames. No v2 icons were created.

The user explicitly authorized resizing beyond standard keyshapes where it improves recognition. The 37 custom envelopes are recorded in `model/contracts/exceptions.v1.json` with this request as their approval. Canvas size remains 48 and stroke width remains 4; spacing and other validation rules were not relaxed.

## Evidence

- `live-feedback.json`: production feedback captured before authoring.
- `before/`: original model backups.
- `changes.json`: each repair, old/new SVG hashes and original module path.
- `final-qa.json`: all 43 build QA rows; every status is `pass`.
- `comparison-light-1.png` through `comparison-light-4.png`, plus matching dark sheets: all 43 compared at native 48 px and enlarged size and visually reviewed.
- `index.html`: searchable before-and-after gallery with light/dark view.
- `before-svg/` and `after-svg/`: exact compared artwork.
- `build.log`: targeted 43-icon build exited 0.
- `tests.log`: 68 focused primitive, profile, parallel-spacing, internal-spacing and symmetry tests passed.

All 43 exported SVGs were verified byte-for-byte against their revised models, and their hashes match the saved build QA. The local gallery is rebuilt. Production API review statuses were not changed in this batch.

## Repairs

| Icon | Change | QA |
| --- | --- | --- |
| animal-print-bird | Replace ambiguous droplets with two staggered three-toed bird tracks. | Pass |
| baby-bottle | Narrow feeding bottle with a projecting teat, collar and two measurement ticks. | Pass |
| cough | Keep the left-facing anatomical head and add two expelled breath strokes at the mouth. | Pass |
| loading-bar | Restore the low horizontal capsule and show a partial progress fill with visible empty space. | Pass |
| mixed-reality-headset | Widen and flatten the visor, preserve the nose recess and show the side strap. | Pass |
| mobile-phone-with-home-button | Restore a tall narrow handset with a top speaker and round home button; remove the false screen divider. | Pass |
| molecule-science | Use a central atom, three satellites and exposed bonds instead of a heavy triangular network. | Pass |
| moon-right | Make the illuminated crescent slimmer, with rounded outer curvature and long inward-curving horns. | Pass |
| mosquito | Add a long proboscis and bent paired legs to an elongated insect body, with two broad wings. | Pass |
| moth | Show the broad triangular forewings, lower wing lobes, central body and antennae. | Pass |
| mother-and-daughter-wearing-headscarves | Restore separate face openings inside two draped scarves, with an unmistakably taller adult beside a child. | Pass |
| mountain-forest-trail | Give the scene a winding foreground trail, a triangular mountain and a recognizable pine tree. | Pass |
| moustache-with-drooping-ends | Flatten the over-tall moustache and restore broad curling lobes with drooping tips. | Pass |
| nautilus-shell | Use a round coiled shell with an expanding outer chamber and flared aperture. | Pass |
| nearly-full-battery | Restore a low battery silhouette, attached terminal and three equal charge bars with one empty slot. | Pass |
| north-direction-marker | Use a true upward navigation needle above an upright capital N. | Pass |
| notion-cube-logo | Restore a larger upright N on the front face and reduce the perspective depth. | Pass |
| notion-logo | Restore the upright serif N and soften the square enclosure corners. | Pass |
| one-world-trade-center | Make the tower tall and slender, with its spire and tapering triangular glass facets. | Pass |
| open-quote | Use two clearly open quotation marks with rounded lower bowls and sweeping upper hooks. | Pass |
| opera-house-shells-on-water | Restore overlapping curved sail roofs over a low waterfront base, with a separate water ripple. | Pass |
| orca-head | Restore a rounded snout, swept dorsal profile, oval eye patch and curved white lower jaw boundary. | Pass |
| oval-light-bulb | Use an elongated glass bulb that narrows naturally into a distinct screw base and rounded contact. | Pass |
| oval-stadium-with-three-flags | Restore an open oval arena with a curved front wall and 3 triangular flags. | Pass |
| oval-stadium-with-two-flags | Restore an open oval arena with a curved front wall and 2 triangular flags. | Pass |
| overlapping-clouds | Replace the rear circular disc with a scalloped cloud silhouette, partially hidden by the foreground cloud. | Pass |
| owl-wearing-mortarboard | Restore the owl body and large paired eyes under a broad diamond mortarboard with tassel. | Pass |
| paw-print | Restore a broad three-lobed central paw pad and arrange four toes in an arch. | Pass |
| paw-print-small-outer-toes | Restore a broad three-lobed central paw pad and arrange four toes in an arch, with smaller outer toes. | Pass |
| peacock-with-spread-tail | Add a scalloped fan tail, separate feather eyes, a bird head with beak and small feet. | Pass |
| pear-shaped-vase | Restore a narrow flared mouth, inward neck and smooth pear-shaped belly with a flat foot. | Pass |
| pelican-on-water | Restore the long bill with throat pouch, curved neck, rounded floating body and water line. | Pass |
| penguin-looking-down | Restore the downturned beak, upright tapered body, belly division and flat feet. | Pass |
| perched-bird | Restore a hooked beak, eye, folded wing and a visible branch beneath the bird. | Pass |
| perched-songbird | Give the rounded songbird a distinct projecting beak, small eye, folded wing and branch perch. | Pass |
| perching-bird | Restore a rounded breast, pointed beak, visible eye, folded wing and branch instead of a wedge silhouette. | Pass |
| person-at-picnic-table | Separate the bent seated torso and forearm from the tabletop, with a clear bench and splayed table legs. | Pass |
| person-connected-to-six-nodes | Restore a recognizable central head-and-shoulders avatar surrounded by six connected circular nodes. | Pass |
| person-crossing-street | Restore a walking stride with an upright torso and a row of crossing stripes beneath the pedestrian. | Pass |
| person-enjoying-sunny-day | Show a relaxed person with raised open arms under a round sun with rays, removing the ambiguous cloud fragment. | Pass |
| person-pointing-at-map-board | Make the arm point visibly to a winding route on a freestanding board, with a complete upright person. | Pass |
| person-receiving-cheek-massage | Show a relaxed face with two closed eyes and a curved hand pressing the cheek, with a visible wrist. | Pass |
| person-recording-with-headphones | Restore a profile wearing a headphone band and ear cup beside a broad studio microphone on a stand. | Pass |

## Follow-up redraw of nine icons

The nine icons flagged in the subsequent visual review were redrawn again in place. The comparison gallery now shows their latest models. See [nine-redraw-20260917](../nine-redraw-20260917/REVIEW.md) for the focused comparison, preserved intermediate drawings and fresh verification.
