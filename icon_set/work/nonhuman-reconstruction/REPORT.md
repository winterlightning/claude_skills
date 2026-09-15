# Nonhuman reconstruction audit

83 canonical icons reconstructed and visually reviewed. All 83 pass the final per-icon model, hole, internal-spacing and overlay-distance checks. The selected official build and refreshed overlay results are recorded in `build.log` and `overlays.log`.

Scope: 180 icons captured from the Failed gallery. 79 human subjects skipped. Five nonhuman sources were removed elsewhere during review. No variant modules were created.

## Construction approach

Inspected original rendered strokes and centerlines, then re-authored Python geometry in place. Used shared attachment nodes, smooth arcs and Bézier curves; retained meaningful sharp corners. Lucide references: armchair, shopping-bag, battery-charging, fish, dog, flame, plane, shirt and box. Detailed per-icon construction plans are in `audit.json` and the review page.

## Remaining 13 nonhuman blockers

### bowling-pins-row

Tested a passing simplification, then rejected it at native size because it weakened the recognizable subject. Original retained for a more faithful redesign.

- qa-overlays distance: lowest line distance 6.65 on centerlines; requires at least 8.0

### bowling-pins-three

Tested a passing simplification, then rejected it at native size because it weakened the recognizable subject. Original retained for a more faithful redesign.

- qa-overlays distance: lowest line distance 6.65 on centerlines; requires at least 8.0

### dailybooth-logo

Tested a passing simplification, then rejected it at native size because it weakened the recognizable subject. Original retained for a more faithful redesign.

- mic [bubble]: bubble and camera are 3.60555 apart on centerlines nearest (36, 34)<->(34, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [camera]: camera and lens are 3 apart on centerlines nearest (24, 31)<->(24, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

### kakaotalk-logo

TALK is crowded inside the speech bubble: several letter gaps are 4–6 units and the A counter is undersized. The complete word needs more room than the framed layout supplies at the required eight-unit spacing. Original retained for manual review.

- mic [bubble]: bubble and t-top are 4.46809 apart on centerlines nearest (6.50716, 15.2136)<->(10, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [bubble]: bubble and l are 6.18949 apart on centerlines nearest (38.9559, 32.7604)<->(35, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [t-stem]: t-stem and a are 6 apart on centerlines nearest (13, 28)<->(19, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [t-top]: t-top and a-bar are 7.81025 apart on centerlines nearest (16, 18)<->(21, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

### line-logo

The N has six-unit parallel strokes, the other letters have five-unit gaps, and LINE is too close to the speech-bubble wall. Retained the full original wordmark; removing letters or the bubble would change its identity.

- mic [letter-e]: parallel straight edges letter-e-2 and letter-n-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [letter-n]: parallel straight edges letter-n-3 and letter-n-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [letter-n]: parallel straight edges letter-n-1 and letter-i are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [letter-e]: parallel straight edges letter-e-1 and e-middle are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)

### line-logo-square

The nested frame and bubble leave only three-unit gaps in LINE, plus a five-unit frame gap and an undersized hole. Retained the original for manual review; the complete nested brand cannot be preserved by simply widening these strokes.

- mic [e]: parallel straight edges e-2 and n-3 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [e]: parallel straight edges e-2 and n-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
- mic [n]: parallel straight edges n-3 and n-1 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [n]: parallel straight edges n-3 and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)

### linux-mint-logo

The L and three M stems are six units apart, with only four units to the enclosing frame. Widening the four stems and the frame gaps exceeds this layout. Retained the original rather than dropping letters.

- mic [m-right-stem]: parallel straight edges m-right-stem and m-middle are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [m-middle]: parallel straight edges m-middle and m-left-stem are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [m-left-stem]: parallel straight edges m-left-stem and l-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [l]: parallel straight edges l-1 and frame-notch-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)

### linux-mint-logo-circle

The L and M stems have six-unit gaps and the outer circular frame is also too close. The required wider letter group does not fit the inner circle at its current height. Retained the complete original for manual review.

- mic [m-right-stem]: parallel straight edges m-right-stem and m-middle are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [m-middle]: parallel straight edges m-middle and m-left-stem are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [m-left-stem]: parallel straight edges m-left-stem and l-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [frame]: frame and m-right-stem are 7.79313 apart on centerlines nearest (40.399, 35.4482)<->(34, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

### long-sporting-rifle

Both an enlarged barrel and a single-stroke barrel pass QA, but the native-size studies read as a bottle or screwdriver instead of a sporting rifle. Restored the original and retained the failed distance evidence.

- qa-overlays distance: lowest line distance 6.57 on centerlines; requires at least 8.0

### meetup-wordmark

The six-letter script has two-unit gaps between the e letters, crowded m/u/p strokes and four undersized holes. A faithful script construction with the required clearances was not established. Original wordmark retained for manual review.

- mic [m-left]: parallel straight edges m-left-1 and m-mid are 5.82086 apart on centerlines (ink gap 1.82086); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [m-mid]: parallel straight edges m-mid and m-right-1 are 5.82086 apart on centerlines (ink gap 1.82086); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [e-base-0]: parallel straight edges e-base-0-1 and e-base-1-1 are 4.94975 apart on centerlines (ink gap 0.949747); requires at least 8 centerline / 4 ink (overlap-fallback)
- mic [e-base-0]: e-base-0 and e-base-1 are 2 apart on centerlines nearest (25, 30)<->(27, 30); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

### microsoft-dynamics-logo

The wider outline passes QA after removing the lower fold, but that fold carries the Dynamics ribbon identity. Restored the original: its lower diagonal still creates a 1.99-unit gap and a pinched wedge.

- holes/pinches: 0 undersized holes; 1 pinches
- qa-overlays distance: lowest line distance 1.99 on centerlines; requires at least 8.0
- qa-overlays holes/pinches: 0 undersized holes; 1 pinches

### react-logo

Tested shared orbit minor radii 8,9,11,12,13,14 against the original 10. Every layout retains 6–12 undersized inter-orbit holes; do not fill these holes or waive the gate.

- holes/pinches: 6 undersized holes; 0 pinches
- qa-overlays holes/pinches: 6 undersized holes; 0 pinches

### wedding-car-with-heart-balloon

The reconstruction passes QA with a shifted roof and separated wheels, but the open body reads as a cart at native size. Restored the original car; the balloon/roof and wheel/body spacing still require a more faithful layout.

- qa-overlays distance: lowest line distance 5.8 on centerlines; requires at least 8.0

## Reconstructed icons

- **airchair** — Lucide armchair: shared arched back and two rounded arms; broad eight-unit seat band and aligned legs.
- **aircraft-releasing-bomb** — Broaden the main wing by moving its paired trailing-edge nodes together; preserve the bomb outline below.
- **airplane-departing-runway** — Move the far wing away from the tailplane while preserving the diagonal body and detached runway.
- **airplane-diagonal** — Lucide plane: widen both wing tips and tail fins coherently; preserve the diagonal fuselage and rounded nose.
- **airplane-other** — An upright aircraft constructed about one axis: broaden swept wing bands and the tailplane, with a rounded nose and exact mirrored nodes.
- **airplane-taking-off** — Move the far-wing root forward along the fuselage and preserve the exact shared attachment.
- **airplane-with-landing-wheel** — Move the far-wing group forward to open the tail clearance; retain the wheel and its actual strut junction.
- **anteater** — Trace the original long downward snout and domed back, replacing the angular ghost-like head; the snout and two legs have shared eight-unit bands.
- **arrow-thick-down-3** — Preserve the downward outlined arrow, broadening its shaft and paired diagonal head bands about the vertical axis.
- **bathrobe** — Lucide shirt principles: open sleeve ends, a broad V collar and clean waist; curved flared hem preserves the robe silhouette without pinched folds.
- **bathrobe-with-tied-belt** — Lucide shirt: balanced shoulders and sleeves, broad wrap panels and tangent rounded hem; belt and tie share one waist node.
- **battery-charging-vertical** — Lucide battery-charging: broad rounded housing, shared terminal nodes and an open lightning stroke with longer turns.
- **brain-side-view-with-stem** — Broaden stem at its shared lower lobe so the interior neck has genuine clearance.
- **brick-firewall** — Wall owns two eight-unit brick courses and staggered joints. One broad smooth flame replaces cramped short tongues; flame silhouette remains asymmetric.
- **burning-crashed-aircraft** — Broaden the broken aircraft wing and trace one flowing flame rising from two exact attachment nodes; retain the smoke trail.
- **climbing-airliner** — Rebuild the broad upper wing around two forward attachment nodes, preserving the rounded climbing nose.
- **crescent-head-wrench** — Broaden the diagonal shaft at its owning neck; retain crescent jaws and the rounded handle end.
- **curled-raccoon** — Open the face-to-tail gap, retain a clear eye and coherent circular back, and put two stripes on the broadest parts of the curl.
- **cushioned-handle-pliers** — Broaden the upper cushioned handle at its outer end, preserving all jaw and pivot nodes.
- **damaged-shipping-box** — Lucide box: preserve shared perspective corners; represent the torn seam with a broad visible break instead of squeezing a zigzag against the bottom edge.
- **dog-carrying-ball** — Trace the rounded muzzle and flowing open jaw instead of the angular zigzag; retain the pointed ear and ball at the mouth.
- **dog-jumping-through-hoop** — Widen the forward leg as a complete paired outline, retaining the dog mid-jump through its hoop.
- **dog-offering-paw** — Trace the seated dog and raised paw with a smooth extended foreleg and rounded haunch; broaden the neck and paw counter.
- **dog-wearing-recovery-cone** — Trace the rounded muzzle and ear above the recovery cone; preserve one straight shared cone rim and open the full head counter.
- **element-reallity-kit-1** — Adjust the shared lower-cube roof station uniformly so the isometric cube faces clear their opposing diagonals.
- **fast-train-nose** — Trace one streamlined nose with tangent cubic joins; move the windscreen divider to form a broad window and a full eight-unit band above the floor.
- **flying-rocket-exhaust-streaks** — Smooth nose curves share broad fin roots; retain the diagonal launch and two well-separated exhaust streaks, omitting the cramped porthole.
- **folding-pocket-knife** — A single smooth cutting edge bows away from the blade back; both blade roots share the rounded handle rim.
- **gear-hierarchy-square-nodes** — Keep the gear and all three equal square child nodes; arrange the children around two sides to give the branches room instead of compressing a horizontal bus.
- **grand-canyon-with-river** — Broaden both cliff shoulders and use a smooth river bend; preserve the sun, distant ridge and open canyon between two cliffs.
- **grizzly-head-profile** — Trace the rounded bear ear, forehead and muzzle; separate the open lips by nine units and rebuild the lower jaw as one smooth contour.
- **hand-saw** — A broad rounded handle surrounds one clear opening. Reduce the blade to three strong teeth with clean shared roots, preserving its diagonal direction.
- **handmade-bag** — Lucide shopping-bag: rounded body and symmetric dome handle joined at the rim; remove cramped dangling handle ends.
- **hanging-spider** — One capsule body owns four equally spaced leg roots per side and a hanging thread; mirrored legs diverge to preserve clearance.
- **heart-pierced-by-arrow** — Move the complete heart away from the arrowhead; show the shaft entering and leaving its outline, with the middle naturally hidden behind the heart.
- **hologram-cube-projector** — Increase all cube face heights together, retaining shared perspective junctions; base and projection beams remain detached with clearance.
- **hot-glue-gun** — Broaden the nozzle and grip around a continuous outline, keeping the diagonal glue-gun profile and a smooth glue bead underneath.
- **hyena-head-profile** — Trace a broad rounded upright ear and a smooth muzzle-to-jaw flow, replacing the narrow angular lower-jaw fold; keep the natural profile asymmetry.
- **inkscape-logo** — Keep the peaked mountain and ink-shaped base, using coherent curves and a smaller detached snow chevron with room on every side.
- **jet-ski-motion** — Broaden the hull band by raising the upper bow station; preserve the handle, speed marks and wave.
- **leaning-tower-of-pisa** — One tilted shaft owns parallel floor stations; reduce four cramped storeys to three wider bands while preserving the lean and ground line.
- **lever-tap-with-droplet** — A clean single-stroke operating lever replaces the narrow outlined blade; broad tap body and rounded drop retain identity.
- **lightning-with-wrench** — Lengthen both lightning turns to open the opposing diagonal edges, retaining the existing curved wrench.
- **magic-wand** — A larger regular five-point head has a broad central counter; the wand joins one exact lower point.
- **outlined-lambda** — Broaden the descending left stroke at its owning junction, keeping the lambda outline and terminal shapes.
- **pencil-cup** — Two upright tools share the cup rim. Equal-width pencil shaft avoids tapered crowding; cup has tangent rounded corners.
- **pencil-marking-ballot** — Use one straight eight-unit pencil shaft and a centred tip; preserve the two ballot boxes and their cross mark.
- **personal-watercraft** — A broad deck band, smooth stern and exact seat/post attachment replace the pinched diagonal deck; preserve the raised handle and open hull ends.
- **pet-carrier-with-straps** — Broad rounded carrier with parallel straps at shared rim/base stations; Lucide bag corner construction.
- **plane** — Open the rear fuselage band by moving its lower shared corner; retain the smooth nose and wing curves.
- **plumed-battle-helmet** — A smooth dome and broad cheek guard define the empty helmet. Widen the crest gap and remove the cramped neck fragments beneath the helmet.
- **pointed-crystal-cluster** — One central crystal and a mirrored pair, with broad parallel side facets and exact shared junctions.
- **poodle-head** — Trace the original poodle haircut: three broad crown puffs above a long face and paired ears. Shared roots preserve the silhouette and open facial counter.
- **potala-palace** — Preserve the terraced hillside palace with broader tiers; simplify the cramped narrow annex wall and finial while retaining the stepped roofline.
- **propeller-plane** — Broaden the entire tail root while preserving the oblique propeller disc and the main wing.
- **pump-action-shotgun** — Broaden the pump assembly and expose its two exact attachment nodes on the barrel; preserve the diagonal stock and long muzzle.
- **pyup-logo** — Move the entire upper P counter down by one unit to clear the outer hexagonal border.
- **rate-stretch-tool** — Two mirrored rounded turns with open arrowheads replace folded duplicate segments; separate their inner endpoints by ten units.
- **restaurant-fork-knife** — Lucide-style table cutlery: equally spaced fork tines and a coherent rounded butter-knife blade; remove the pinched blade taper.
- **rocking-horse** — Trace a wider neck and rounded back into two legs, with a smooth belly and one continuous curved rocker.
- **satellite-with-signal-waves** — Mirrored solar panels connect at their nearest corners to a small circular bus; longer rods replace cramped face attachments. Preserve the broadcast arc.
- **sawmill** — Broaden the lowest blade tooth at its shared valley, retaining the irregular saw profile and broad arched opening.
- **sea-lion** — Trace the sitting sea lion with a long neck and broad smooth haunch. Widen both flippers and remove the redundant cramped flipper mark.
- **shopping-bag-with-loop-handle** — Preserve the tapered shopping bag using coherent curved sides tangent to the rounded base; the dome handle ends exactly at the rim.
- **shopping-cart-large-open-wheels** — Deepen the rounded basket uniformly, preserving two large circular wheels and a shared handle attachment.
- **spider-web** — Six radiating threads meet bowed silk spans; remove the crowded second ring so each web sector retains an open counter.
- **standing-horse** — Horse silhouette retains pointed ear, muzzle, two clear legs and curved tail. Paired leg widths share eight-unit spacing; directional stance remains asymmetric.
- **standing-stag** — Trace a clear neck and muzzle with a rounded back and belly. The branching antler rises from the forehead, with its tips held away from the head.
- **star-fireworks** — Three symmetric open starbursts replace tiny filled star outlines; genuine shared ray centres own the trails.
- **straight-bodied-missile** — Widen both fin roots together along the hull diagonals; preserve the pointed body and exhaust.
- **suspended-succulent-planter** — Raise the suspension shoulders and rebuild the succulent leaf as two coherent curves; preserve the wide elliptical bowl.
- **swimming-dog** — A domed head and smooth rump rise above four equal waves. Deepen the muzzle to provide a full eight-unit opening.
- **swimming-shark** — Widen tail throat at both shared roots, preserving the crescent fin and curved body.
- **text-flow-rows** — Three equal rounded text nodes and a clear stepped flow; all links meet explicit nodes, with separated turns and one output arrow.
- **three-engine-spacecraft** — Symmetric arched cabin, circular window and three equal eight-unit engine openings; replace narrow flared nozzle necks.
- **three-heart-plant-in-shallow-pot** — A rounded three-leaf cluster fits the circle envelope, reaching radius twenty at the bowl base. Smaller smooth leaves, separated stems and a broad bowl preserve all three hearts.
- **three-heart-plant-in-square-pot** — Three equal smooth heart leaves use the radial envelope to keep their spacing; a square pot owns three separated stem attachments.
- **three-light-ceiling-fixture** — Three broad trapezoidal lamp shades share one canopy and equal cord stations. Stagger heights to separate shades; omit the short top cord.
- **three-way-text-sign** — Open the W by giving it upright outer strokes and broad diagonal valleys; keep all four literal glyphs and the two-row layout.
- **triceratops-head-side** — Open the beak at its actual lips instead of retaining a cramped angular notch; keep the horn and frill curves.
- **turreted-chateau-hotel** — Broaden the right annex to give the entry gable a full eight-unit band; preserve the pitched roofs and turret.
- **vr-headset-side-view** — Rebuild the visor with shared strap stations and consistent corner radii; widen the rear folded band and preserve the smooth overhead strap.
- **whale-with-spout** — Trace the original whale: smooth rounded body, a broad raised tail throat and a separate water spout. Preserve natural directional asymmetry.

## Final validation

- Official selected build: exit 0; all 83 checked icons exported.
- Refreshed QA overlays: 83 distance passes, 83 negative-space passes. Six drawings have no eligible distance candidate; the checker reports those as unmeasured passes.
- Exact publication verification: 83/83 SVGs and overlay fingerprints match the reviewed files.
- Gallery tests requiring local servers: 29/29 passed after rerunning outside the network sandbox.
- Published corpus consistency tests: 4/4 passed after the final build.
- Full suite: 391 tests ran; the initial run reported 26 failures and 29 sandbox network errors, with one skip. The network errors and stale publication comparisons were resolved by the reruns above. The whole suite is not green: held icons, a skipped human figure and existing catalog/skill/trace fixtures remain failing. See tests.log, network-tests.log and dist-tests.log.

The [icon-solo skill](/Applications/Workspaces/pictographic/claude_skills/.agents/skills/icon-solo/SKILL.md) says: “a reported blocker beats a weakened rule.” No exception was used to turn an unresolved drawing into a pass.

## Final keyshapes

Rectangular keyshapes retain the appropriate tall, wide or square envelope; the two three-heart plants use the radial CIRCLE envelope to preserve their spread.

- airchair: VRECT_L
- aircraft-releasing-bomb: HRECT_XL
- airplane-departing-runway: SQUARE
- airplane-diagonal: SQUARE
- airplane-other: SQUARE
- airplane-taking-off: SQUARE
- airplane-with-landing-wheel: SQUARE
- anteater: HRECT_L
- arrow-thick-down-3: SQUARE
- bathrobe: SQUARE
- bathrobe-with-tied-belt: VRECT_L
- battery-charging-vertical: VRECT_L
- brain-side-view-with-stem: SQUARE
- brick-firewall: HRECT_L
- burning-crashed-aircraft: VRECT_L
- climbing-airliner: HRECT_L
- crescent-head-wrench: SQUARE
- curled-raccoon: SQUARE
- cushioned-handle-pliers: SQUARE
- damaged-shipping-box: SQUARE
- dog-carrying-ball: SQUARE
- dog-jumping-through-hoop: HRECT_L
- dog-offering-paw: SQUARE
- dog-wearing-recovery-cone: SQUARE
- element-reallity-kit-1: SQUARE
- fast-train-nose: HRECT_L
- flying-rocket-exhaust-streaks: SQUARE
- folding-pocket-knife: SQUARE
- gear-hierarchy-square-nodes: SQUARE
- grand-canyon-with-river: SQUARE
- grizzly-head-profile: SQUARE
- hand-saw: SQUARE
- handmade-bag: VRECT_L
- hanging-spider: VRECT_L
- heart-pierced-by-arrow: SQUARE
- hologram-cube-projector: VRECT_L
- hot-glue-gun: SQUARE
- hyena-head-profile: HRECT_L
- inkscape-logo: SQUARE
- jet-ski-motion: SQUARE
- leaning-tower-of-pisa: SQUARE
- lever-tap-with-droplet: VRECT_L
- lightning-with-wrench: SQUARE
- magic-wand: SQUARE
- outlined-lambda: SQUARE
- pencil-cup: VRECT_L
- pencil-marking-ballot: SQUARE
- personal-watercraft: HRECT_L
- pet-carrier-with-straps: SQUARE
- plane: HRECT_L
- plumed-battle-helmet: VRECT_L
- pointed-crystal-cluster: VRECT_L
- poodle-head: SQUARE
- potala-palace: HRECT_L
- propeller-plane: SQUARE
- pump-action-shotgun: SQUARE
- pyup-logo: VRECT_L
- rate-stretch-tool: SQUARE
- restaurant-fork-knife: VRECT_L
- rocking-horse: SQUARE
- satellite-with-signal-waves: SQUARE
- sawmill: SQUARE
- sea-lion: SQUARE
- shopping-bag-with-loop-handle: VRECT_L
- shopping-cart-large-open-wheels: HRECT_L
- spider-web: SQUARE
- standing-horse: HRECT_L
- standing-stag: SQUARE
- star-fireworks: HRECT_L
- straight-bodied-missile: SQUARE
- suspended-succulent-planter: VRECT_L
- swimming-dog: HRECT_L
- swimming-shark: SQUARE
- text-flow-rows: SQUARE
- three-engine-spacecraft: HRECT_L
- three-heart-plant-in-shallow-pot: CIRCLE
- three-heart-plant-in-square-pot: CIRCLE
- three-light-ceiling-fixture: HRECT_L
- three-way-text-sign: SQUARE
- triceratops-head-side: SQUARE
- turreted-chateau-hotel: SQUARE
- vr-headset-side-view: HRECT_L
- whale-with-spout: SQUARE

Live gallery verification: HTTP 200 review page; all 83 repaired icons absent from Failed; all 13 held icons still present; five representative served SVGs match the reviewed bytes exactly.
