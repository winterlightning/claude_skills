"""broccoli-and-carrot (redraw of the new-pipeline traced SVG).

Plan: a broccoli on the left and an upright carrot on the right, side by side
on HRECT_M (centerline box (4,10)-(44,38)), each mirrored about its own axis.
- broccoli (axis x=15): one closed outline. Two side florets r5 centred
  (9,21)/(21,21) (the left one gives the x=4 extreme) and a top floret that is
  a semicircle r6 between the upper notches (9,16)/(21,16), apex (15,10) on the
  top extreme. The notches are deliberate corners, as in the generated image.
  The stalk leaves the floret bottoms (9,26)/(21,26) as concave r16 arcs
  narrowing to a waist about 10 wide, then meets the base line (10,38)-(20,38)
  on the bottom extreme.
- carrot (axis x=39): shoulder semicircle r5 centred (39,23), 34..44 wide,
  with the right edge giving the x=44 extreme. The sides are r25 arcs centred
  (19,23)/(59,23), tangent to the shoulder (so there is no kink there), meeting
  at the point (39,38) on the bottom extreme. The outline is split at the apex
  (39,18) so the two leaf strokes share that endpoint and are declared
  `connect`. The leaves diverge to (34,10)/(44,10) on the top extreme.
The broccoli's right floret stays about 8.1 from the carrot shoulder and side
(both curved, so above the exact-8 minimum).
Lucide `broccoli` (a crown built from round florets, with corner notches between
them) informed the crown. Lucide `carrot` is a diagonal, three-leaf drawing, so
only its idea of a tapered body plus separate leaf strokes was used. Both are
drawn upright here, to follow the generated image.

Metric issues (broccoli-and-carrot_metrics.json) and how they were handled:
- stroke-width (info, 2.4 traced): redrawn at stroke 4, with every gap
  budgeted for it.
- keyshape-short-axis (SQUARE fills 73% of y, needs a 1.37 stretch): I changed
  the keyshape to HRECT_M, the metrics' second candidate (score 0.96, stretch
  1.05). Stretching this pair to 36 tall would make the broccoli a narrow column
  (the carrot's clearance keeps it 22 wide). HRECT_M keeps the image's
  proportions, and all four extremes are touched exactly.
- clearance e0/e3 (carrot vs broccoli, 2.98) and e1/e3 (leaf vs broccoli,
  7.95): the broccoli now ends at x=26 and the carrot starts at x=34. The
  nearest pair is about 8.1 on centerlines, and the leaves are more than 12
  from the crown.
- loose-join e1/e2 (leaves 1.03 apart): both leaves start at the carrot apex
  (39,18), sharing the exact endpoint with the outline, and are declared
  `connect`.
- hole at (37.6, 20.8) 4.44 wide: the carrot is 10 wide on centerlines at the
  shoulder, so its opening is 6 inscribed. The leaf V no longer closes a hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1833535f-220e-490a-9e51-7058a14ac9db"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1923-broccoli-and-carrot/broccoli-and-carrot_raw.svg"
AUTHOR = "claude-opus-5-5"

# Broccoli: one closed outline mirrored about x=15.
BX = 15
LOBE_R, LOBE_DX, LOBE_Y = 5, 6, 21      # side floret centres (9,21) / (21,21)
CROWN_R = 6                              # top floret: semicircle between the notches (9,16)/(21,16), apex (15,10)
BASE_Y, BASE_HALF = 38, 5                # stalk base (10,38)-(20,38)
STALK_R = 16                             # concave stalk walls (waist ~10 wide)
# Carrot: closed outline mirrored about x=39, leaves joined at the top.
CX, CAR_R, SHOULDER_Y = 39, 5, 23        # shoulder semicircle (34..44, apex y=18)
SIDE_R, TIP_Y = 25, 38                   # side arcs tangent to the shoulder, meet at the tip
LEAF_Y, LEAF_DX = 10, 5


class BroccoliAndCarrotRedraw(Solo48):
    icon_id = "broccoli-and-carrot-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vegetables"
    aliases = ("vegetables", "veggies")
    keywords = ("broccoli", "carrot", "vegetable", "vegan", "healthy", "food", "produce", "grocery")

    def build(self) -> None:
        # Broccoli outline, clockwise from the base's left corner.
        r, dx, ly = LOBE_R, LOBE_DX, LOBE_Y
        lx, rx = BX - dx, BX + dx
        self.add_arc("stalk-left", (BX - BASE_HALF, BASE_Y), (lx, ly + r), radius_x=STALK_R, sweep=False)
        self.add_arc("floret-left-low", (lx, ly + r), (lx - r, ly), radius_x=r)
        self.add_arc("floret-left-high", (lx - r, ly), (lx, ly - r), radius_x=r)
        self.add_arc("floret-top", (lx, ly - r), (rx, ly - r), radius_x=CROWN_R)
        self.add_arc("floret-right-high", (rx, ly - r), (rx + r, ly), radius_x=r)
        self.add_arc("floret-right-low", (rx + r, ly), (rx, ly + r), radius_x=r)
        self.add_arc("stalk-right", (rx, ly + r), (BX + BASE_HALF, BASE_Y), radius_x=STALK_R, sweep=False)
        self.add_line("stalk-base", (BX + BASE_HALF, BASE_Y), (BX - BASE_HALF, BASE_Y))
        self.add_contour(
            "broccoli", "stalk-left", "floret-left-low", "floret-left-high", "floret-top",
            "floret-right-high", "floret-right-low", "stalk-right", "stalk-base", closed=True,
        )

        # Carrot outline, clockwise from the left shoulder; split at the top for the leaves.
        cr, sy, top = CAR_R, SHOULDER_Y, SHOULDER_Y - CAR_R
        self.add_arc("carrot-shoulder-left", (CX - cr, sy), (CX, top), radius_x=cr)
        self.add_arc("carrot-shoulder-right", (CX, top), (CX + cr, sy), radius_x=cr)
        self.add_arc("carrot-side-right", (CX + cr, sy), (CX, TIP_Y), radius_x=SIDE_R)
        self.add_arc("carrot-side-left", (CX, TIP_Y), (CX - cr, sy), radius_x=SIDE_R)
        self.add_contour(
            "carrot", "carrot-shoulder-left", "carrot-shoulder-right",
            "carrot-side-right", "carrot-side-left", closed=True,
        )
        self.add_line("leaf-left", (CX, top), (CX - LEAF_DX, LEAF_Y))
        self.add_line("leaf-right", (CX, top), (CX + LEAF_DX, LEAF_Y))
        self.relate("connect", "leaf-left", "carrot")
        self.relate("connect", "leaf-right", "carrot")
        self.relate("connect", "leaf-left", "leaf-right")
