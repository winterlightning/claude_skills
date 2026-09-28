"""bearded-pirate-behind-a-laptop (redraw of the new-pipeline traced SVG).

Plan: a pirate's head in a tricorne hat, peeking over the lid of a laptop
seen from behind. VRECT_L (centerline box (8,4)-(40,44)), mirrored about
x=24 with m()/mm().
- face: one circle, r10 about (24,22). Its top arc (16,16)-(24,12)-(32,16)
  is also the hat's lower edge, so the hat sits on the head. The cheeks run
  down to the side points (14,22)/(34,22).
- beard: from each side point, a sideburn drops to a tooth at (14,26), cuts
  back to a notch at (17,24) and runs down to the beard point (24,34). This is
  the jagged V beard from the PNG. The tooth is exactly 8 above the laptop
  edge.
- hat: the PNG's tricorne. Wings run from the head at (16,16) out to the tips
  (8,12)/(40,12). Concave sides rise to humps at (17,4)/(31,4), with a front
  notch at (24,7). Every crown point stays 8+ from the head arc.
- laptop: the lid's back is a trapezoid with its top edge at (10,34)-(38,34)
  and its legs standing on the base line (8,44)-(40,44) at x=13/35. The beard
  point rests on the lid's top edge (a shared node, relate connect), which
  reads as the pirate sitting behind the laptop.
Extremes: left 8 (hat tip, base), right 40, top 4 (humps), bottom 44 (base).
4 contours: hat, face, lid, base.
References: icon_set/references/human_ref/user.svg (circular outlined head).
No detached torso is drawn: the lid hides the body, so there is no head and
torso pair and no mark_human_figure flag. The head-to-body gap rule does not
apply to a head resting on an unrelated object. Lucide `laptop` informed the
lid-on-a-base-line construction; it has no pirate hat.

Metric issues (bearded-pirate-behind-a-laptop_metrics.json):
- keyshape-short-axis (SQUARE, x filled 73%): switched to VRECT_L, the
  metrics' third candidate (x 0.91 / y 1.0 fill), which suits the tall 0.73
  subject. All four extremes are exact. On SQUARE, the hat, face, beard,
  shoulders and laptop could not stack at 8 spacing, and the head came out
  squashed.
- clearance e0/e1, e0/e2, e0/e3 (hat 1.9-7.1 from the head and sideburns):
  fixed. The hat's lower edge is the head's own top arc (shared nodes), and
  the crown is 8+ above it everywhere.
- clearance e1-e9 among the head, sideburns (e2, e3), beard zigzag (e4),
  beard sides (e5, e6), shoulders (e7, e8), tie (e9) and lid (e10) (1.7-7.7):
  fixed. The head, sideburns and beard are one face contour, with one
  tooth/notch per side instead of the small zigzag. The shoulders and tie are
  dropped (see below).
- hole [21.2,9.9] 1.6 and [23.9,18.0] 3.5 (hat sliver and a small head
  ring): fixed. The hat hole spans the crown (4-7) to the head top (12-16),
  and the face hole is the whole r10 face. Build-gate holes pass.
- hole [21.3,28.5] / [26.6,28.6] 1.4 (beard zigzag slivers): fixed. The
  zigzag is gone, and each tooth is an open jag on the outer edge.
- hole [18.8,35.6] 4.8 (the laptop's thin base capsule): fixed. The base is
  a single line, and the lid hole is 10 tall.
- loose-join e2/e1, e2/e5, e3/e1, e3/e6, e4/e5, e4/e6, e8/e10, e9/e4: fixed.
  Every contact is a shared integer node declared with relate("connect")
  (face/hat, face/lid, lid/base).
- no-head (no circle traced as the head): fixed. The head is a true r10
  circle.
- stroke-count (12 strokes, budget 6): now 4 contours.
- stroke-width (2.37 trace): redrawn at stroke 4, with every gap budgeted at
  8.
Dropped: the shoulders and the tie line. With the hat, face, beard and lid at
stroke 4, there is no 8-unit band for a body between the beard and the lid
(the SQUARE and VRECT_L attempts squashed the head to under 12 units).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "aa4f64c4-a374-44b3-9890-7cd9bfe00eab"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1732-bearded-pirate-behind-a-laptop/bearded-pirate-behind-a-laptop_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_C = (24, 22)        # face circle centre
HEAD_R = 10              # top y=12, sides x=14/34
HAT_ON = (16, 16)        # (-8, -6) on the face circle: the hat wing leaves the head
BEARD = ((14, 26), (17, 24))   # sideburn tooth (8 above the laptop) and notch
TOP = 34                 # laptop screen top edge; the beard point rests on it
BASE = 44
TIP = (8, 12)            # hat wing tip
HUMP = (17, 4)           # crown hump
NOTCH = (AXIS, 7)        # front notch of the tricorne


def m(p):
    """Mirror about the vertical axis x = 24."""
    return (2 * AXIS - p[0], p[1])


def mm(*pts):
    return tuple(m(q) for q in pts)


class BeardedPirateBehindALaptopRedraw(Solo48):
    icon_id = "bearded-pirate-behind-a-laptop-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("pirate at laptop", "pirate programmer", "pirate hacker")
    keywords = ("pirate", "beard", "tricorne", "hat", "laptop", "computer", "piracy", "hacker")

    def build(self) -> None:
        bz = self.add_bezier
        a = self.add_arc
        r = HEAD_R
        cx, cy = HEAD_C
        crown_top = (cx, cy - r)
        side = (cx - r, cy)
        chin = (AXIS, TOP)
        # hat: its lower edge is the head's top arc; wings out to the tips,
        # concave sides up to two humps and a front notch
        wing = ((12, 15), (9, 14))
        rise = ((12, 10), (14, 4))
        dip = ((21, 4), (23, 6))
        a("head-top-l", HAT_ON, crown_top, radius_x=r, sweep=True)
        a("head-top-r", crown_top, m(HAT_ON), radius_x=r, sweep=True)
        bz("wing-r", m(HAT_ON), mm(*wing, TIP))
        bz("crown-r", m(TIP), mm(*rise, HUMP), mm(*dip, NOTCH))
        bz("crown-l", NOTCH, (dip[1], dip[0], HUMP), (rise[1], rise[0], TIP))
        bz("wing-l", TIP, (wing[1], wing[0], HAT_ON))
        self.add_contour("hat", "head-top-l", "head-top-r", "wing-r", "crown-r", "crown-l", "wing-l", closed=True)
        # face: round cheeks under the hat, pointed beard down to the laptop
        a("cheek-l", HAT_ON, side, radius_x=r, sweep=False)
        beard = (side,) + BEARD + (chin,)
        ids = ["cheek-l"]
        for i in range(len(beard) - 1):
            self.add_line(f"beard-l{i}", beard[i], beard[i + 1])
            ids.append(f"beard-l{i}")
        rb = mm(*reversed(beard))
        for i in range(len(rb) - 1):
            self.add_line(f"beard-r{i}", rb[i], rb[i + 1])
            ids.append(f"beard-r{i}")
        a("cheek-r", m(side), m(HAT_ON), radius_x=r, sweep=False)
        self.add_contour("face", *ids, "cheek-r")
        self.relate("connect", "face", "hat")
        # laptop lid seen from behind, standing on the base line
        self.add_line("screen-l", (13, BASE), (10, TOP))
        self.add_line("screen-top-l", (10, TOP), chin)
        self.add_line("screen-top-r", chin, (38, TOP))
        self.add_line("screen-r", (38, TOP), (35, BASE))
        self.add_contour("screen", "screen-l", "screen-top-l", "screen-top-r", "screen-r")
        self.add_line("base-l", (8, BASE), (13, BASE))
        self.add_line("base-m", (13, BASE), (35, BASE))
        self.add_line("base-r", (35, BASE), (40, BASE))
        self.add_contour("base", "base-l", "base-m", "base-r")
        self.relate("connect", "screen", "base")
        self.relate("connect", "face", "screen")
