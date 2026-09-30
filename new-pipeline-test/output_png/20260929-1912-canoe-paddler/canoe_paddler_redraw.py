"""canoe-paddler (redraw of the new-pipeline traced SVG).

Plan: seated paddler in a long open canoe, paddle raised mid-stroke, on
HRECT_M (centerline box (4,10)-(44,38)), the suggested keyshape.
- head: circle r4 (two semicircles) on the torso axis HX=16; top on y=10.
- torso: vertical from the neck (exactly 8 centerline units under the head,
  human-reference.md) down to the keel, so the paddler sits IN the canoe; the
  keel is split at the seat and the hull contour connects to the torso.
- arm: one line from the neck down-right to the hand on the shaft end (it
  leaves the neck level/downward, so it never closes on the head).
- canoe: one open contour mirrored about x=24: flat keel y=38 (the bottom
  extreme) and two cubic ends rising to raked, upswept tips at (4,30) and
  (44,30) (the x extremes). No gunwale line, as the brief asks.
- paddle: shaft along (3,-4) from the hand to a hollow stadium blade whose
  half-width (4,3) is exactly 5, so every node is an integer point; the end arc
  is split at its y=10 and x=44 apexes.
Design notes: the traced pose (blade in the water beside the bow) was tried
first. A 10-wide hollow blade + 8 clearance leaves the canoe only 18 units long
and it read as a tub/anchor at 48 px. A full-width canoe with the paddle raised
reads as canoeing; with a deep bowl hull the raised-paddle version read as a
face or a pot, hence the shallow 8-deep hull.
References: icon_set/references/human_ref/full_body_ref.png (circle head,
round-ended single-stroke limbs); pictographic-primitives/recreation
"canoe person" (this source id) and "sport kayaking" for the long shallow hull
with the torso sunk into it. No useful Lucide match (no canoe/paddle icon).

Metric issues (canoe-paddler_metrics.json):
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (HRECT_M y fill 76%): fixed, head top y=10, blade top
  y=10, keel y=38, tips x=4, blade x=44 all sit exactly on the box.
- clearance e0/e2 (head dot 4.84 from the body): fixed, real r4 head, neck
  exactly 8 below it, marked with mark_human_figure.
- clearance e1/e2 (body 3.43 from the canoe rim): fixed, the torso now
  genuinely joins the keel (shared node, declared connect).
- clearance e1/e3, e1/e4 (canoe vs paddle 4.69 / 2.18): fixed, the paddle
  is raised clear of the canoe (>= 8 everywhere).
- clearance e2/e4 (arm vs paddle 3.36): fixed, the hand now holds the shaft
  (shared endpoint, declared connect).
- holes at (27.1,25.2), (39.7,30.7), (9.3,31.6) (< 6 inscribed): fixed, the
  doubled hull wall and body/rim pockets are gone; the only enclosed hole is
  the blade, 10 wide on centerlines = 6 inscribed.
- no-head: fixed, the head is a true circle.
Nothing was left unrepaired. Trade-off: the paddle is raised rather than
dipped in the water (see design notes), and its shaft is short because any
tail below the hand would come within 7 of the keel.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fc6689dd-a028-5cb2-b326-1fe893e5518c"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1912-canoe-paddler/canoe-paddler_raw.svg"
AUTHOR = "claude-opus-5-5"

HX = 16                     # figure axis
HEAD_R = 4
HEAD_CY = 14                # head top on y=10
NECK_Y = HEAD_CY + HEAD_R + 8
# canoe: full width 4..44, mirrored about x=24; upswept tips on TIP_Y, flat
# keel y=38 from KEEL_END either side; each end is one cubic.
HULL_L, HULL_R, TIP_Y, KEEL_Y, KEEL_END = 4, 44, 30, 38, 12
# paddle: axis direction (3,-4) up-right, blade half-width (4,3)
HAND, NECK_OF_BLADE = (30, 27), (33, 23)
BLADE_A, BLADE_B, BLADE_R = (36, 19), (39, 15), 5


class CanoePaddlerRedraw(Solo48):
    icon_id = "canoe-paddler-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("canoeist", "canoeing", "paddler")
    keywords = ("canoe", "paddle", "paddling", "boat", "rowing", "water sports", "kayak")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        # Two semicircles: lets the spacing engine prove the exact 8-unit gap
        # from the circle to the neck-level arm run.
        self.add_arc("head-top", (cx - r, cy), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-bottom", (cx + r, cy), (cx - r, cy), radius_x=r, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        neck, seat = (HX, NECK_Y), (HX, KEEL_Y)
        self.add_line("torso", neck, seat)
        self.mark_human_figure("paddler", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", neck, HAND)
        self.relate("connect", "arm", "torso")

        # Canoe: stern tip -> keel (split where the torso sits) -> bow tip.
        kl, kr = HULL_L + KEEL_END, HULL_R - KEEL_END
        # Tip tangent leans outward (1:2) so the ends read as a canoe's rake.
        self.add_bezier("hull-stern", (HULL_L, TIP_Y),
                        ((HULL_L + 2, TIP_Y + 4), (HULL_L + 6, KEEL_Y), (kl, KEEL_Y)))
        self.add_line("hull-keel-aft", (kl, KEEL_Y), seat)
        self.add_line("hull-keel-fore", seat, (kr, KEEL_Y))
        self.add_bezier("hull-bow", (kr, KEEL_Y),
                        ((HULL_R - 6, KEEL_Y), (HULL_R - 2, TIP_Y + 4), (HULL_R, TIP_Y)))
        self.add_contour("hull", "hull-stern", "hull-keel-aft", "hull-keel-fore", "hull-bow")
        self.relate("connect", "hull", "torso")

        # Paddle raised for the next stroke: the hand grips the shaft end.
        (ax, ay), (bx, by), br = BLADE_A, BLADE_B, BLADE_R
        self.add_line("shaft", HAND, NECK_OF_BLADE)
        self.relate("connect", "shaft", "arm")

        # Blade outline, clockwise from the neck; the far end arc is split at
        # its y=10 and x=44 apexes so it lands on the keyshape exactly.
        left_a, right_a = (ax - 4, ay - 3), (ax + 4, ay + 3)
        left_b, right_b = (bx - 4, by - 3), (bx + 4, by + 3)
        self.add_arc("blade-neck-l", NECK_OF_BLADE, left_a, radius_x=br, sweep=True)
        self.add_line("blade-left", left_a, left_b)
        self.add_arc("blade-end-1", left_b, (bx, by - br), radius_x=br, sweep=True)
        self.add_arc("blade-end-2", (bx, by - br), (bx + br, by), radius_x=br, sweep=True)
        self.add_arc("blade-end-3", (bx + br, by), right_b, radius_x=br, sweep=True)
        self.add_line("blade-right", right_b, right_a)
        self.add_arc("blade-neck-r", right_a, NECK_OF_BLADE, radius_x=br, sweep=True)
        self.add_contour(
            "blade", "blade-neck-l", "blade-left", "blade-end-1", "blade-end-2",
            "blade-end-3", "blade-right", "blade-neck-r", closed=True,
        )
        self.relate("connect", "blade", "shaft")
