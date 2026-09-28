"""broccoli and carrot: a broccoli head on a flared stalk beside an upright
carrot with two leaf sprigs (redraw of the new-pipeline traced SVG).

Plan: HRECT_M (centerline box (4,10)-(44,38)), as suggested (fit 1.0 on y).
- broccoli, axis x=15: one closed crown of three lobes: side lobes r6
  semicircles about (10,21)/(20,21) reach x 4 and 26, a top lobe r5
  semicircle about (15,15) reaches y 10, and a shallow r7 underside arc
  (bulging 2) closes it between the side-lobe bottoms (10,27)/(20,27).
  The stalk is an open contour from those two nodes, flaring by 2 to a
  flat foot on y 38 (8..22), connected to the crown.
- carrot, axis x=39: an r5 shoulder semicircle (34..44 at y 22, apex
  (39,17)) and a straight taper to the tip (39,38).
- leaves: two r7 arcs from the carrot apex to (34,10)/(44,10), curling
  outward, mirrored about x=39 and connected to the carrot.
Extremes: x 4 (left lobe) / 44 (carrot shoulder, right leaf tip),
y 10 (top lobe, leaf tips) / 38 (stalk foot, carrot tip) -- exact.

Metric issues fixed by the rebuild:
- clearance e0/e1, e0/e2, e1/e2 (leaf loops touching each other and the
  carrot, 0-1.8): the loops became two open sprigs sharing the apex node
  with the carrot (declared connect), their tips 10 apart.
- clearance e0/e4 (6.98) and e2/e4 (3.18), leaves and carrot vs crown:
  the crown ends at x 26, the carrot at x 34; the closest pair (right
  lobe vs carrot shoulder) is 8.04 on centerlines.
- hole at (16.4,32.6) (2.97, the stalk): the stalk interior is now 10-14
  wide and 9 tall below the crown underside (>= 8.9 from the foot).
- hole at (36.7,21.3) (5.34, the carrot body): a 10-wide shoulder over a
  16-tall taper gives an inscribed width over 6.
- keyshape-short-axis (x 97%): every extreme sits on the HRECT_M box.
- stroke-width (2.55): drawn at the profile stroke 4, gaps budgeted for it.
Not kept, with reason: closed lens leaves (a 6-unit hole needs a leaf about
10 wide on centerlines; the 7 units above the carrot cannot hold two) and
the fourth crown bump (the 22-wide crown holds three lobes with holes and
cusps that stay readable at 48 px).
Lucide: `carrot` (tapered root, sprig leaves) informed the carrot; no
useful Lucide broccoli, the crown is a three-lobe cloud built on the axis.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1833535f-220e-490a-9e51-7058a14ac9db"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1721-broccoli-and-carrot/broccoli-and-carrot_raw.svg"
AUTHOR = "claude-opus-5-5"

CROWN_X = 15          # broccoli axis
LOBE_R = 6            # side lobes, centres (CROWN_X -/+ 4, 20)
TOP_R = 5             # top lobe, centre (CROWN_X, 14)
CROWN_BASE = 27       # side lobe bottoms = stalk tops
BASE_R = 7            # crown underside, bulges 2 into the stalk
FLARE = 2             # stalk flare each side at the foot
FOOT = 38
CARROT_X = 39
SHOULDER_Y = 22       # carrot shoulder semicircle r6, apex y 16
TIP = 38
LEAF = (5, 7)
LEAF_R = 7         # leaf run (dx, dy) from the carrot apex


class BroccoliAndCarrotRedraw(Solo48):
    icon_id = "broccoli-and-carrot-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vegetables"
    aliases = ("vegetables", "broccoli carrot")
    keywords = ("broccoli", "carrot", "vegetables", "food", "healthy", "vegan", "groceries", "produce")

    def build(self) -> None:
        cx, r = CROWN_X, LOBE_R
        lx, rx = cx - 5, cx + 5
        a, b = (lx, CROWN_BASE), (rx, CROWN_BASE)
        v1, v2 = (lx, CROWN_BASE - 2 * r), (rx, CROWN_BASE - 2 * r)
        self.add_arc("lobe-left", a, v1, radius_x=r, sweep=True)
        self.add_arc("lobe-top", v1, v2, radius_x=TOP_R, sweep=True)
        self.add_arc("lobe-right", v2, b, radius_x=r, sweep=True)
        self.add_arc("crown-base", b, a, radius_x=BASE_R, sweep=True)
        self.add_contour("crown", "lobe-left", "lobe-top", "lobe-right", "crown-base", closed=True)
        self.add_line("stalk-left", a, (lx - FLARE, FOOT))
        self.add_line("stalk-foot", (lx - FLARE, FOOT), (rx + FLARE, FOOT))
        self.add_line("stalk-right", (rx + FLARE, FOOT), b)
        self.add_contour("stalk", "stalk-left", "stalk-foot", "stalk-right")
        self.relate("connect", "crown", "stalk")

        k, s = CARROT_X, 5
        left, right, apex = (k - s, SHOULDER_Y), (k + s, SHOULDER_Y), (k, SHOULDER_Y - s)
        self.add_arc("shoulder-left", left, apex, radius_x=s, sweep=True)
        self.add_arc("shoulder-right", apex, right, radius_x=s, sweep=True)
        self.add_line("root-right", right, (k, TIP))
        self.add_line("root-left", (k, TIP), left)
        self.add_contour("carrot", "shoulder-left", "shoulder-right", "root-right", "root-left", closed=True)
        dx, dy = LEAF
        self.add_arc("leaf-left", apex, (k - dx, apex[1] - dy), radius_x=LEAF_R, sweep=False)
        self.add_arc("leaf-right", apex, (k + dx, apex[1] - dy), radius_x=LEAF_R, sweep=True)
        self.relate("connect", "carrot", "leaf-left")
        self.relate("connect", "carrot", "leaf-right")
