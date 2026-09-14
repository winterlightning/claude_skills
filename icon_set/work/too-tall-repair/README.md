# Ink box too tall — repair review

27 repaired variants cover 30 failed entries; five combined references have ten component briefs queued. Originals are preserved, so their historical failures remain visible.

All revised models pass without warnings. The selected solo build exits 0. Both themes were inspected at native 48 px. The full repository test suite was run but is not green: it includes existing invalid corpus icons and sandbox-blocked server tests. Missing exports for these new variants during that earlier run are checked separately after the build.

VRECT_L is used for upright subjects: ink (6,2)–(42,46). SQUARE is used for broad faces and scenes: ink (4,4)–(44,44). No validation constants changed.

Human reference: `icon_set/references/human_ref/full_body_ref.png`. Adult head radius 5; baby head radius 3. Nearest adult head/body centerlines: (18,16)–(18,24). Baby: (36,28)–(28,28). Both gaps are exactly 8 centerline / 4 visible ink units.

| Revised icon | Keyshape | Change | Construction reference |
|---|---|---|---|
| ceres-astrological-symbol-v2 | VRECT_L | Shortened cup tips and lower stem; retained the sickle cup and cross. | No useful exact match. |
| cow-head-with-horns-v2 | SQUARE | Raised the muzzle while retaining horns and ears; split the crown at its horn attachment. | No useful exact match. |
| crescent-moon-v2 | VRECT_L | Reduced both elliptical heights together; retained the left-facing opening. | moon: coherent outer and inner curves. |
| lance-leaf-plant-in-rounded-pot-v2 | VRECT_L | Lowered the crown tip and raised the pot base; retained all three leaves. | No useful exact match. |
| matryoshka-doll-v2 | VRECT_L | Rebalanced the dome, circular face and rounded base; retained the scarf. | No useful exact match; face is an inset doll feature, not a detached human head. |
| middle-click-mouse-v2 | VRECT_L | Moved capsule end centers inward with unchanged circular radius; retained the wheel. | mouse: tangent capsule ends. |
| narrow-necked-vase-v2 | VRECT_L | Shortened the lip and moved the rounded belly base upward. | amphora: paired neck-to-belly flow; no handles added. |
| proserpine-astrological-symbol-v2 | VRECT_L | Adjusted the two opposed elliptical bowls; retained the cross between them. | No useful exact match. |
| saturn-astrological-symbol-v3 | VRECT_L | Shortened the stem and sickle extent, keeping the asymmetric hook. | No useful exact match. |
| scorpio-zodiac-symbol-v3 | SQUARE | Lowered both equal humps together; preserved the directional sting. | No useful inspected exact match. |
| selene-astrological-symbol-v3 | VRECT_L | Moved the lunar arc as one unit and shortened the lower stem. | moon: coherent lunar curve. |
| shepherds-crook-v2 | VRECT_L | Inset the hook and shaft ends; smoothed the leaning shaft into a tangent hook. | No useful exact match. |
| shopping-bag-with-loop-handle-v3 | VRECT_L | Moved the handle dome and base inward; preserved the tapered bag and split the handle at its true attachment. | shopping-bag: coherent handle and rounded lower corners. |
| stemmed-chalice-v2 | VRECT_L | Inset rim and foot; retained the bowl, stem and triangular foot. | wine: bowl-to-stem attachment. |
| two-button-mouse-v2 | VRECT_L | Moved the equal capsule ends inward and retained both button divisions. | mouse: tangent capsule construction. |
| usb-symbol-v2 | VRECT_L | Inset the arrow and root circle without changing branch terminals. | usb: branching shaft and distinct terminals; intentional asymmetry. |
| whale-tail-v2 | SQUARE | Raised the waves and shortened the lower tail to restore clear separation. | No useful exact match. |
| wireless-mouse-v2 | VRECT_L | Inset equal capsule ends and moved the wheel for a certified gap. | mouse: tangent capsule and single wheel stroke. |
| wolf-face-v3 | SQUARE | Raised the chin and nose together, retaining pointed ears and paired cheeks. | No useful exact match. |
| cd-rom-drive-v3 | SQUARE | Moved the emerging circular disc upward; joined the shallow housing at the slot corners. Solid concentric hub retained. | disc-3: concentric circular construction. |
| gem-with-jewellers-pliers-v3 | VRECT_L | Opened the gem facet band and inset the handle ends and joint. | gem: pointed outline and a single broad facet. |
| winter-mitten-v3 | VRECT_L | Inset the dome and base; widened the cuff band to eight centerline units. Right thumb remains asymmetric. | No useful exact match. |
| analogue-wristwatch-v5 | VRECT_L | Used an oval dial to retain eight-unit strap bands inside the upright envelope; retained two hands. | watch: centered dial with paired attached straps. |
| bird-flock-v3 | SQUARE | Replaced crowded miniature heads and bodies with five repeated paired wings, arranged 2/1/2. Covers both older flock versions. | bird: reduced curved silhouette; no exact flock match. |
| dress-v3 | VRECT_L | Widened both straps, inset the hem, and retained the scoop neck and flared skirt. | No useful exact match. |
| diaper-change-v4 | SQUARE | Rebuilt the bending adult and supine baby with circular heads, a single arm/leg and separated changing surface. Covers all three older versions. | human_ref/full_body_ref.png: bending action, circular heads and round limbs. |
| eagle-head-front-v2 | SQUARE | Inset the feather hem; joined the paired brows to an open hooked beak to remove crowding. Small closed beak removed. | bird: coherent head curve and reduced beak; no exact front eagle match. |

## Component splits

The icon-making skill says: “Do not create the combined icon or an edited variant of the combination.” It also says: “Stop after queuing a rejected combined reference unless the user also requested generating its components.”

Source: `.agents/skills/icon-making/SKILL.md`. The five source splits were queued locally as IDs 123–127. Component generation remains pending; no combined variant was authored.

- Left-click mouse → left-button mouse (solo) + left click arc (sub).
- Right-click mouse → right-button mouse (solo) + right click arc (sub).
- Wireless mouse with signal → mouse (solo) + wireless signal (sub).
- Tarot card eye → tarot card frame (container) + almond eye (sub).
- Tarot card moon → tarot card frame (container) + crescent moon (sub).

[Light comparison](preview-light.png) · [Dark comparison](preview-dark.png) · [Validation details](full-validation.json)
