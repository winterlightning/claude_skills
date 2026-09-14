# Wide and tall keyshape repairs

Reviewed all **135** entries from “Ink box too wide & too tall”.

- **123 new independent variants**, plus **2 existing validated repairs**, cover **127 standalone entries**.
- **8 combined references** were split into **16 queued component briefs**.
- Every repaired variant is valid without warnings, passes internal-spacing review, appears in the SOLO48 manifest, and exactly matches its exported SVG.
- All 135 parent model files remain unchanged.

[Open the comparison gallery](index.html) · [Verification record](verification.json) · [Test log](tests.log)

## Bounds and appearance

The keyshape fit uses the existing zero-tolerance rule. Stroke width remains 4 and the integer grid remains 1; no validation thresholds were changed for this repair. The four extrema are:

| Keyshape | Visible ink envelope | Variants |
| --- | --- | ---: |
| SQUARE | (4,4)–(44,44) | 70 |
| VRECT_L | (6,2)–(42,46) | 38 |
| HRECT_L | (2,6)–(46,42) | 17 |

Square envelopes support balanced, near-equal subjects; tall envelopes support upright objects; wide envelopes support horizontal structures and layouts that need more lateral clearance. Some drawings were rebalanced or simplified when the old layout could not preserve clear openings.

Every candidate was reviewed enlarged and at 48 pixels in light and dark themes. The comparison sheets are grouped below; the gallery also includes the two reused repairs.

- Sheet 1: [light](preview-light-1.png) · [dark](preview-dark-1.png)
- Sheet 2: [light](preview-light-2.png) · [dark](preview-dark-2.png)
- Sheet 3: [light](preview-light-3.png) · [dark](preview-dark-3.png)
- Sheet 4: [light](preview-light-4.png) · [dark](preview-dark-4.png)
- Sheet 5: [light](preview-light-5.png) · [dark](preview-dark-5.png)

The original rendered icon was the primary reference for every repair. Local Lucide `monitor` and its atomic-debug geometry informed the screen frames and stands; Lucide `link` and its atomic-debug geometry informed the paired open-link construction. Earlier reference study from these repair batches also covered beads/gems, hats, bags, animals, amphorae and other shared object components. Intentional asymmetry remains in directional symbols, profile busts, tools, hanging objects, plants and scenes.

Human figures follow `icon_set/references/human_ref/full_body_ref.png` and `user.svg`: circular heads and exactly **4 units of visible detached head-to-body clearance**. Actual measured pairs for the infant, action figure, fortune teller, geisha and two-person group are recorded in `verification.json`. Anatomically continuous profile busts and physical masks/helmets retain their intrinsic connections.

## Component handoffs

The [icon-making skill](../../../.agents/skills/icon-making/SKILL.md) says: “Do not create the combined icon or an edited variant of the combination.” These entries were therefore handed off instead of exported as new combined primitives. Original models and exports remain available.

| Original | Standalone components |
| --- | --- |
| left-double-click-mouse | Computer mouse (solo) + Left double-click arcs (sub) |
| right-double-click-mouse | Computer mouse (solo) + Right double-click arcs (sub) |
| monitor-download-arrow | Desktop monitor frame (container) + Down arrow (sub) |
| monitor-upload-arrow | Desktop monitor frame (container) + Up arrow (sub) |
| monitor-in-security-shield | Security shield outline (container) + Desktop monitor glyph (sub) |
| knight-helm-on-shield | Heraldic shield outline (container) + Knight helmet glyph (sub) |
| open-locket-with-portrait | Open oval locket frame (container) + Portrait bust (sub) |
| figured-ceremonial-urn | Ceremonial urn enclosure (container) + Person emblem (sub) |

All eight queue operations succeeded in the local Pending briefs database. The full handoff records are in [splits.json](splits.json).

## Validation

The selected-family build checked all 125 chosen variants and exited successfully. Direct model validation and export/manifest consistency checks also passed for every chosen variant. Parent hashes and complete coverage of the 135-entry target list were verified.

Full repository test outcome: **Ran 335 tests in 229.956s; FAILED (failures=1592, errors=26, skipped=1)**. The suite remains red from existing invalid/review corpus entries, existing source/generated-artifact checks and server tests blocked by sandbox socket permissions. No failure heading names any of these 125 repaired variants. The scoped 125-variant build and direct validations passed. See [the test log](tests.log).

Browser automation blocked navigation to the local file URL, so the gallery controls were not exercised in-browser. Static gallery asset links were checked; icon appearance was reviewed from direct light/dark renders.

## Individual repairs

| Original entries | Variant | Keyshape | Changes |
| --- | --- | --- | --- |
| aries-zodiac-symbol | [aries-zodiac-symbol-v2](../../dist/solo48/aries-zodiac-symbol-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| baby-figure + baby-figure-v2 | [baby-figure-v5](../../dist/solo48/baby-figure-v5.svg) | VRECT_L | Circular six-unit infant head and shoulder station24 give exactly four units of visible clearance; kept stick arms and diaper. |
| baby-head | [baby-head-v6](../../dist/solo48/baby-head-v6.svg) | SQUARE | Extended paired shoulder ends to the square envelope; kept curl, cheeks and ears. |
| bangle-with-heart-charm | [bangle-with-heart-charm-v2](../../dist/solo48/bangle-with-heart-charm-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| bathrobe-with-tied-belt | [bathrobe-with-tied-belt-v2](../../dist/solo48/bathrobe-with-tied-belt-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| beaded-loop-with-heart-charm | [beaded-loop-with-heart-charm-v3](../../dist/solo48/beaded-loop-with-heart-charm-v3.svg) | SQUARE | Moved the two beads beside the charm outward to restore clearance without changing the loop topology. Rebuilt matching circular heart lobes around the shared tip and link. |
| beaded-necklace-with-hexagon-stone | [beaded-necklace-with-hexagon-stone-v3](../../dist/solo48/beaded-necklace-with-hexagon-stone-v3.svg) | SQUARE | Two readable circular beads, shared wire attachments and the hexagonal pendant. Removed the two smaller bead pairs. |
| beading-wire-with-beads | [beading-wire-with-beads-v2](../../dist/solo48/beading-wire-with-beads-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| beer-mug-with-foam | [beer-mug-with-foam-v2](../../dist/solo48/beer-mug-with-foam-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| bobble-hat-with-panelled-cuff | [bobble-hat-with-panelled-cuff-v3](../../dist/solo48/bobble-hat-with-panelled-cuff-v3.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| bobble-hat-with-seams | [bobble-hat-with-seams-v4](../../dist/solo48/bobble-hat-with-seams-v4.svg) | HRECT_L | Kept a circular four-unit pompom at the shared crown apex. |
| bobble-hat | [bobble-hat-v2](../../dist/solo48/bobble-hat-v2.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| bud-branch-in-pitcher | [bud-branch-in-pitcher-v2](../../dist/solo48/bud-branch-in-pitcher-v2.svg) | VRECT_L | One circular bud and two twigs above the pitcher; retained the handle and spout. |
| cat-paw-print | [cat-paw-print-v2](../../dist/solo48/cat-paw-print-v2.svg) | SQUARE | Four round solid toe pads and a broad lower pad; removed the undersized hollow toe rings. |
| cave-painting-symbols | [cave-painting-symbols-v2](../../dist/solo48/cave-painting-symbols-v2.svg) | SQUARE | Separated the branch strokes and shortened the neighboring arch above the diamond. |
| chinese-dragon-head | [chinese-dragon-head-v2](../../dist/solo48/chinese-dragon-head-v2.svg) | SQUARE | Replaced angled eye strokes with paired round dots, retaining horns, muzzle and whiskers. Broadened the paired cheek stations to clear the eyes. Flattened the paired muzzle arches to clear the eyes. Removed the lower muzzle divider because its small enclosed opening cannot survive the required stroke. |
| classical-head-with-book | [classical-head-with-book-v2](../../dist/solo48/classical-head-with-book-v2.svg) | SQUARE | Moved the face and neck station left to clear the physical book. Shortened the back-of-head ending above the open book. |
| classical-statue-bust | [classical-statue-bust-v2](../../dist/solo48/classical-statue-bust-v2.svg) | VRECT_L | Raised the bust base to leave four units of ink clearance above the plinth. Rebuilt the profile and shoulder silhouette with a broad base and a clear plinth gap, omitting the tiny chin ledge. |
| classical-temple-facade | [classical-temple-facade-v2](../../dist/solo48/classical-temple-facade-v2.svg) | SQUARE | Rebalanced column and step stations for equal legal separations. |
| cobra-head-friendly | [cobra-head-friendly-v2](../../dist/solo48/cobra-head-friendly-v2.svg) | VRECT_L | Removed the crowded inner face outline; retained the flared hood, neck and paired eyes. Separated the two eyes symmetrically. |
| collar-necklace-with-pearl | [collar-necklace-with-pearl-v2](../../dist/solo48/collar-necklace-with-pearl-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| column-with-open-book | [column-with-open-book-v3](../../dist/solo48/column-with-open-book-v3.svg) | SQUARE | Reduced the shaft to one stroke and opened its gap below the capital; retained the book scene. Removed the tiny inward scroll hooks while retaining the paired rounded capital ends. |
| computer-memory-module | [computer-memory-module-v3](../../dist/solo48/computer-memory-module-v3.svg) | HRECT_L | Reauthored horizontally with two equal chips and three shared contact pins so both chip openings remain readable. |
| crystal-ball-on-stand | [crystal-ball-on-stand-v2](../../dist/solo48/crystal-ball-on-stand-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| cuffed-beanie | [cuffed-beanie-v2](../../dist/solo48/cuffed-beanie-v2.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| curved-monitor | [curved-monitor-v3](../../dist/solo48/curved-monitor-v3.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| deer-head | [deer-head-v2](../../dist/solo48/deer-head-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| descending-lunar-node-symbol | [descending-lunar-node-symbol-v2](../../dist/solo48/descending-lunar-node-symbol-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| desktop-monitor-bezel-splayed-stand | [desktop-monitor-bezel-splayed-stand-v2](../../dist/solo48/desktop-monitor-bezel-splayed-stand-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| desktop-monitor-centre-post-stand | [desktop-monitor-centre-post-stand-v2](../../dist/solo48/desktop-monitor-centre-post-stand-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| desktop-monitor-curved-pedestal | [desktop-monitor-curved-pedestal-v2](../../dist/solo48/desktop-monitor-curved-pedestal-v2.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| desktop-monitor-pedestal-stand | [desktop-monitor-pedestal-stand-v2](../../dist/solo48/desktop-monitor-pedestal-stand-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| desktop-monitor-splayed-stand | [desktop-monitor-splayed-stand-v2](../../dist/solo48/desktop-monitor-splayed-stand-v2.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| desktop-monitor-twin-post-stand | [desktop-monitor-twin-post-stand-v2](../../dist/solo48/desktop-monitor-twin-post-stand-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| distressed-baby-face | [distressed-baby-face-v2](../../dist/solo48/distressed-baby-face-v2.svg) | SQUARE | Round baby face, ears and frown with simple eye dots; removed crowded eye crosses and stress rays. |
| dog-face-tall-ears | [dog-face-tall-ears-v2](../../dist/solo48/dog-face-tall-ears-v2.svg) | VRECT_L | Inset paired eyes and raised the nose one unit for certifiable curved clearances. |
| drop-earrings-with-diamond-beads | [drop-earrings-with-diamond-beads-v2](../../dist/solo48/drop-earrings-with-diamond-beads-v2.svg) | VRECT_L | Narrowed the inward diamond tips to retain four units of clear ink between the earrings. |
| elephant-head-friendly | [elephant-head-friendly-v2](../../dist/solo48/elephant-head-friendly-v2.svg) | HRECT_L | Broadened the forehead and shared ear attachments to make room for paired eyes, preserving the long trunk. |
| feathered-war-bonnet | [feathered-war-bonnet-v2](../../dist/solo48/feathered-war-bonnet-v2.svg) | SQUARE | Lowered the forehead band with attached side pendants and simplified paired feather barbs. Shortened the inward feather barbs equally. Inset the paired feather bases away from the central feather. |
| figure-with-outstretched-limbs | [figure-with-outstretched-limbs-v2](../../dist/solo48/figure-with-outstretched-limbs-v2.svg) | SQUARE | Kept the action pose and round head; rebuilt the arm stations with an exact eight-unit head-to-body centerline gap. Separated the true horizontal arm stroke so its exact head clearance is certified. |
| flaming-brazier | [flaming-brazier-v2](../../dist/solo48/flaming-brazier-v2.svg) | VRECT_L | Shortened the flame ends to clear the bowl rim. |
| floppy-disk-with-label | [floppy-disk-with-label-v2](../../dist/solo48/floppy-disk-with-label-v2.svg) | SQUARE | Inset the shutter and label; removed the crowded slot and writing mark. |
| floppy-disk | [floppy-disk-v5](../../dist/solo48/floppy-disk-v5.svg) | SQUARE | Inset shutter and label sides and used a solid hub mark to preserve the floppy disk structure. |
| fluffy-lamb-front | [fluffy-lamb-front-v2](../../dist/solo48/fluffy-lamb-front-v2.svg) | SQUARE | Elongated face and paired ears inside four broad fleece lobes, with two small feet. |
| folding-hand-fan | [folding-hand-fan-v3](../../dist/solo48/folding-hand-fan-v3.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| fortune-teller-reading | [fortune-teller-reading-v2](../../dist/solo48/fortune-teller-reading-v2.svg) | SQUARE | Rebuilt the seated human with a circular head, exact four-unit detached gap and a clear physical crystal-ball scene. Shortened the tabletop near the reaching hand. |
| gaming-keyboard-with-cable | [gaming-keyboard-with-cable-v3](../../dist/solo48/gaming-keyboard-with-cable-v3.svg) | SQUARE | Reduced the key rows to a single broad key strip and raised the cable loop to clear the case. |
| geisha-bust | [geisha-bust-v2](../../dist/solo48/geisha-bust-v2.svg) | VRECT_L | Circular head, top bun, paired hairpins and broad shoulders. Exact four-unit visible head-to-body gap; removed the small collar folds. |
| gemini-zodiac-symbol | [gemini-zodiac-symbol-v2](../../dist/solo48/gemini-zodiac-symbol-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| great-sphinx | [great-sphinx-v2](../../dist/solo48/great-sphinx-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| handbag-with-clasp | [handbag-with-clasp-v2](../../dist/solo48/handbag-with-clasp-v2.svg) | SQUARE | Raised clasp and attached flap together to open the gap above the bag base. |
| handbag-with-curved-flap | [handbag-with-curved-flap-v2](../../dist/solo48/handbag-with-curved-flap-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| handled-amphora-vase | [handled-amphora-vase-v2](../../dist/solo48/handled-amphora-vase-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| hanging-chinese-lanterns | [hanging-chinese-lanterns-v3](../../dist/solo48/hanging-chinese-lanterns-v3.svg) | SQUARE | Lowered the right lantern cap and shared upper attachment; retained the staggered hanging scene. |
| inscribed-stone-tablet | [inscribed-stone-tablet-v2](../../dist/solo48/inscribed-stone-tablet-v2.svg) | VRECT_L | Shortened the middle inscription strokes to leave a clear four-unit gap. |
| interlocking-chain-links | [interlocking-chain-links-v2](../../dist/solo48/interlocking-chain-links-v2.svg) | HRECT_L | Two opposing open links with matched quarter ellipses; preserved the offset arrangement. |
| intertwined-snakes | [intertwined-snakes-v2](../../dist/solo48/intertwined-snakes-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| ionic-column | [ionic-column-v2](../../dist/solo48/ionic-column-v2.svg) | SQUARE | Rebuilt equal circular volutes and an eight-unit plinth depth using shared capital and shaft stations. |
| jackal-head-anubis | [jackal-head-anubis-v2](../../dist/solo48/jackal-head-anubis-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| jewellery-display-bust | [jewellery-display-bust-v2](../../dist/solo48/jewellery-display-bust-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| jupiter-astrological-symbol | [jupiter-astrological-symbol-v2](../../dist/solo48/jupiter-astrological-symbol-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| knight-armor-torso | [knight-armor-torso-v2](../../dist/solo48/knight-armor-torso-v2.svg) | SQUARE | Reduced the visor to a central opening and shortened the helmet chin to clear the armor shoulders. Raised the visor opening one unit. Broadened the helmet and its dome around the centered visor. |
| knit-winter-hat | [knit-winter-hat-v2](../../dist/solo48/knit-winter-hat-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| leo-zodiac-symbol | [leo-zodiac-symbol-v2](../../dist/solo48/leo-zodiac-symbol-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| lidded-ceremonial-urn | [lidded-ceremonial-urn-v3](../../dist/solo48/lidded-ceremonial-urn-v3.svg) | VRECT_L | Rebuilt equal semicircular handles and lowered the neck shoulder station to clear the lid. Raised the vessel baseline to open the pedestal gap. |
| mars-astrological-symbol | [mars-astrological-symbol-v2](../../dist/solo48/mars-astrological-symbol-v2.svg) | SQUARE | Rebuilt the Mars symbol with a true circular ring and a shared integer attachment for the northeast arrow. |
| memory-module-with-notch | [memory-module-with-notch-v3](../../dist/solo48/memory-module-with-notch-v3.svg) | HRECT_L | Reauthored horizontally with equal readable chips and a bottom registration notch. |
| minotaur-bust | [minotaur-bust-v2](../../dist/solo48/minotaur-bust-v2.svg) | SQUARE | Removed the crowded small muzzle mark, keeping the bull horns, ears, chin and broad human shoulders. |
| monitor-with-desk-keyboard | [monitor-with-desk-keyboard-v3](../../dist/solo48/monitor-with-desk-keyboard-v3.svg) | SQUARE | Raised the screen bottom and its shared stand node, retaining keyboard thickness and eight-unit centerline stand height. |
| monkey-face | [monkey-face-v2](../../dist/solo48/monkey-face-v2.svg) | HRECT_L | Broad muzzle, equal ears and two separated eyes; removed the crowded inner face panel. |
| monkey-head | [monkey-head-v3](../../dist/solo48/monkey-head-v3.svg) | HRECT_L | Broad muzzle, equal ears and two separated eyes; removed the crowded inner brow outline. |
| monocle-with-cord | [monocle-with-cord-v2](../../dist/solo48/monocle-with-cord-v2.svg) | SQUARE | Rebuilt a true circular lens and a tangent U-shaped cord reaching the square bottom edge. |
| moose-head | [moose-head-v2](../../dist/solo48/moose-head-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| necklace-bust-form | [necklace-bust-form-v3](../../dist/solo48/necklace-bust-form-v3.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| necklace-display-bust | [necklace-display-bust-v2](../../dist/solo48/necklace-display-bust-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| necklace-with-oval-locket | [necklace-with-oval-locket-v2](../../dist/solo48/necklace-with-oval-locket-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| necklace-with-round-pendant | [necklace-with-round-pendant-v2](../../dist/solo48/necklace-with-round-pendant-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| necklace-with-teardrop-pendant | [necklace-with-teardrop-pendant-v2](../../dist/solo48/necklace-with-teardrop-pendant-v2.svg) | VRECT_L | Raised the necklace bowl apex to separate the pendant by four visible units. |
| necklace-with-three-beads | [necklace-with-three-beads-v4](../../dist/solo48/necklace-with-three-beads-v4.svg) | SQUARE | One large circular pendant bead and two small solid bead attachments; simplified the connecting wire. |
| neptune-astrological-symbol | [neptune-astrological-symbol-v2](../../dist/solo48/neptune-astrological-symbol-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| olive-laurel-wreath | [olive-laurel-wreath-v3](../../dist/solo48/olive-laurel-wreath-v3.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| open-cuff-bangle | [open-cuff-bangle-v2](../../dist/solo48/open-cuff-bangle-v2.svg) | HRECT_L | Widened the cuff band by shrinking the interior opening and using matched rounded ends. |
| open-end-maintenance-wrench | [open-end-maintenance-wrench-v3](../../dist/solo48/open-end-maintenance-wrench-v3.svg) | VRECT_L | Upright open jaw with matched curved returns and a round-ended handle; replaced the narrow diagonal bands. |
| open-folding-fan | [open-folding-fan-v3](../../dist/solo48/open-folding-fan-v3.svg) | HRECT_L | Replaced the tiny hollow pivot with a round-ended pin. |
| open-umbrella-with-ribs | [open-umbrella-with-ribs-v2](../../dist/solo48/open-umbrella-with-ribs-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| open-umbrella-with-scalloped-canopy | [open-umbrella-with-scalloped-canopy-v2](../../dist/solo48/open-umbrella-with-scalloped-canopy-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| orchid-in-shallow-planter | [orchid-in-shallow-planter-v2](../../dist/solo48/orchid-in-shallow-planter-v2.svg) | SQUARE | Reduced crowded petals to three equal round blossoms and gave the shallow planter a full eight-unit depth. |
| organizational-hierarchy-cube | [organizational-hierarchy-cube-v2](../../dist/solo48/organizational-hierarchy-cube-v2.svg) | SQUARE | Broadened the cube faces and replaced tiny child rings with three round-ended branches. |
| otter-with-paws | [otter-with-paws-v2](../../dist/solo48/otter-with-paws-v2.svg) | SQUARE | Rebuilt equal ears and paws; removed tiny whiskers, toe cuts and mouth to keep the paired eyes and nose clear. |
| pair-of-teardrop-earrings + pair-of-teardrop-earrings-v2 | [pair-of-teardrop-earrings-v3](../../dist/solo48/pair-of-teardrop-earrings-v3.svg) | SQUARE | Rebuilt mirrored teardrops with semicircular bases and equal studs; kept the pair eight units apart. |
| pair-of-wedding-rings | [pair-of-wedding-rings-v2](../../dist/solo48/pair-of-wedding-rings-v2.svg) | SQUARE | Rebuilt a circular foreground ring and open rear engagement ring with a readable diamond. Shortened the rear ring opening beside the foreground ring. |
| paired-landscape-window-panels | [paired-landscape-window-panels-v2](../../dist/solo48/paired-landscape-window-panels-v2.svg) | SQUARE | Opened the central frame gap symmetrically while retaining both landscape panels. |
| palmistry-hand | [palmistry-hand-v2](../../dist/solo48/palmistry-hand-v2.svg) | SQUARE | Rebuilt four equal-width finger openings from shared stations, with one readable palm crease. |
| paper-airplane-message-send | [paper-airplane-message-send-v2](../../dist/solo48/paper-airplane-message-send-v2.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| patterned-winter-mitten | [patterned-winter-mitten-v2](../../dist/solo48/patterned-winter-mitten-v2.svg) | VRECT_L | Rebuilt the thumb cap as an exact quarter circle and kept its shared attachment nodes. |
| pharaoh-nemes-mask | [pharaoh-nemes-mask-v3](../../dist/solo48/pharaoh-nemes-mask-v3.svg) | SQUARE | Nemes cloth, face, crest and beard with open drapes; removed the undersized crest box and eye dots. |
| pisces-zodiac-symbol | [pisces-zodiac-symbol-v2](../../dist/solo48/pisces-zodiac-symbol-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| plumed-battle-helmet | [plumed-battle-helmet-v2](../../dist/solo48/plumed-battle-helmet-v2.svg) | VRECT_L | Opened the helmet cheek guards and thickened the returning face rim. |
| potty-with-lid | [potty-with-lid-v2](../../dist/solo48/potty-with-lid-v2.svg) | VRECT_L | Raised the seat and widened the base legs around a smaller round foot opening. |
| record-turntable | [record-turntable-v3](../../dist/solo48/record-turntable-v3.svg) | SQUARE | Broadened the deck and made the platter circular; removed the crowded small control mark. Lowered the platter and tonearm together to clear the deck top. |
| rhombus-chain-links | [rhombus-chain-links-v2](../../dist/solo48/rhombus-chain-links-v2.svg) | SQUARE | Three equal six-unit rhombus links, evenly spaced along the diagonal, with shared connecting nodes. |
| ribbon-bow-with-tails | [ribbon-bow-with-tails-v2](../../dist/solo48/ribbon-bow-with-tails-v2.svg) | SQUARE | Broadened both ribbon tails symmetrically. Spread the tail attachment nodes on the bow return edges. |
| ring-in-presentation-box | [ring-in-presentation-box-v2](../../dist/solo48/ring-in-presentation-box-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| rocking-horse-toy | [rocking-horse-toy-v2](../../dist/solo48/rocking-horse-toy-v2.svg) | HRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| sailboat | [sailboat-v2](../../dist/solo48/sailboat-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| sheep-jumping-fence-v2 | [sheep-jumping-fence-v4](../../dist/solo48/sheep-jumping-fence-v4.svg) | SQUARE | Rebuilt the muzzle with an exact half ellipse and lowered the fence posts away from the jumping sheep. |
| ships-anchor | [ships-anchor-v2](../../dist/solo48/ships-anchor-v2.svg) | SQUARE | Kept the suspension ring circular. |
| shopping-bag-with-arched-handle | [shopping-bag-with-arched-handle-v2](../../dist/solo48/shopping-bag-with-arched-handle-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| simple-open-umbrella | [simple-open-umbrella-v2](../../dist/solo48/simple-open-umbrella-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| sitting-penguin | [sitting-penguin-v2](../../dist/solo48/sitting-penguin-v2.svg) | VRECT_L | Broadened the penguin head and body for two separated eyes and a small round beak, keeping the paired feet. |
| smartwatch | [smartwatch-v3](../../dist/solo48/smartwatch-v3.svg) | SQUARE | Shortened the watch case vertically and moved shared strap nodes together, leaving eight units between the case and strap crests. |
| spartan-helmet | [spartan-helmet-v2](../../dist/solo48/spartan-helmet-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| stacking-ring-toy-v2 | [stacking-ring-toy-v4](../../dist/solo48/stacking-ring-toy-v4.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| sunglasses-with-sun | [sunglasses-with-sun-v2](../../dist/solo48/sunglasses-with-sun-v2.svg) | SQUARE | Widened the bridge gap and reduced the small sun center to a solid dot. |
| three-flying-birds-v2 | [three-flying-birds-v3](../../dist/solo48/three-flying-birds-v3.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| top-hat-with-curved-brim | [top-hat-with-curved-brim-v2](../../dist/solo48/top-hat-with-curved-brim-v2.svg) | SQUARE | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| trilobite-fossil | [trilobite-fossil-v2](../../dist/solo48/trilobite-fossil-v2.svg) | VRECT_L | Removed the crowded head ridge; retained the domed head, segmented body, legs and tail. |
| tropical-island-with-palm-tree | [tropical-island-with-palm-tree-v3](../../dist/solo48/tropical-island-with-palm-tree-v3.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| two-stick-figures | [two-stick-figures-v2](../../dist/solo48/two-stick-figures-v2.svg) | SQUARE | Rebuilt matching circular heads and detached shoulders with exactly four visible units of clearance; retained the joined hands. |
| uranus-astrological-symbol | [uranus-astrological-symbol-v2](../../dist/solo48/uranus-astrological-symbol-v2.svg) | VRECT_L | Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features. |
| witches-cauldron | [witches-cauldron-v3](../../dist/solo48/witches-cauldron-v3.svg) | SQUARE | Shortened and separated the two steam curls while preserving the cauldron silhouette. |
| woolly-lamb-front | [woolly-lamb-front-v2](../../dist/solo48/woolly-lamb-front-v2.svg) | SQUARE | Elongated face and paired ears inside four broad fleece lobes, with two small feet. |
| written-scroll | [written-scroll-v2](../../dist/solo48/written-scroll-v2.svg) | SQUARE | Retained one centered inscription line; removed the lower crowded line to keep the scroll opening readable. Shortened the inscription to clear both scroll walls. |
| scorpio-zodiac-symbol | [scorpio-zodiac-symbol-v3](../../dist/solo48/scorpio-zodiac-symbol-v3.svg) | SQUARE | Reused the validated repair from the preceding batch. |
| cd-rom-drive | [cd-rom-drive-v3](../../dist/solo48/cd-rom-drive-v3.svg) | SQUARE | Reused the validated repair from the preceding batch. |
