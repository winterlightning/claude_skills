"""bee with drooping wings (redraw of the new-pipeline traced SVG).

Plan: an upright bee seen from above, mirrored about x=24, on VRECT_L
(centerline box (8,4)-(40,44), ink (6,2)-(42,46)).
- head: an r5 ring about (24,9); top on y=4. Its bottom point is the
  abdomen apex (24,14), a declared tangent contact (split at the cardinals).
- abdomen: a pill 12 wide (sides x=18/30), r6 caps about (24,20) and
  (24,38), apex y=14, bottom y=44. The sides are split at the two stripes.
- stripes: y=24 and y=34, so apex-stripe, stripe-stripe and stripe-bottom
  are all 10: every band opening is 6 of clear white at stroke 4.
- wings: one drooping lobe per side, not a floating teardrop. The top
  flank leaves the upper-stripe node (18,24) and slopes down and out to
  x=8 (vertical tangent at (8,36)), an r4 bowl rounds the bottom to
  (12,40), and a tangent cubic returns to the cap joint (18,38). The body
  wall closes the lobe. Left built, right mirrored.
Height budget: head 10 + three 10-high abdomen bands = 40, the full height of
VRECT_L. That is why this is not the suggested SQUARE: on SQUARE (36 tall)
the same bee only fit with an r4 head and stripes 8 apart. That version
passed validate_icon and the build gate, but the metrics hole check failed
it (head ring 3.88, stripe band 4.0 wide).
Traced shape: bee-with-drooping-wings_raw.svg and the generated PNG were
read for the subject only; nothing is copied from their coordinates.
Lucide: there is no bee. The pill body, straight cross stripes and round
ring head follow Lucide `bug` / `snail` style construction on this grid.

Metric issues (trace):
- keyshape-short-axis (SQUARE y only 87%): fixed. The bee now touches all
  four VRECT_L extremes exactly (x=8/40 wing edges, y=4 head top, y=44
  body bottom).
- clearance e0/e1 (head vs abdomen 2.47): not 8, see below. It is now an
  exact shared point with a declared connect instead of a near-miss.
- clearance e0/e4, e0/e5 (head vs wings ~7.2-7.4): fixed. The wing root
  moved down to the upper-stripe node, 11 from the head ring.
- clearance e1/e4, e1/e5, e2/e4, e2/e5, e3/e4, e3/e5 (wings 2-4 from the
  abdomen and stripes): the floating wings are now lobes that share
  endpoints with the abdomen wall, so they are joined. Separating them
  instead would need 8 of white between wing and body on each side. With
  a 6-unit wing opening that is 4+8+6+8+12+8+6+8+4 wide, more than every
  keyshape allows, so it was not possible.
- clearance e2/e3 (stripes 4.99 apart): fixed, 10 apart.
- loose-join x4 (stripes 0.9 short of the body): fixed. They end on split
  nodes of the side walls and are declared connected.
- hole x6 (head 4.12, band 4.4, wings 3.93, slivers 1.0/2.8): fixed. On the
  redraw's own metrics every hole is at least 5.82 (all ok) and there are
  no sliver holes.
- stroke-width (info): drawn at stroke 4; every gap is budgeted for 4.
Left on the redraw's own metrics (validate_icon valid, build_gate pass):
- e0/e1 0.0: the head sits on the abdomen apex on purpose. A detached head
  needs 8 more units of height than VRECT_L has with two 10-high stripe
  bands.
- e3/e4, e3/e5 4.0: the wing underside rejoins the wall at the cap joint
  (18,38), 4 below where the lower stripe meets the same wall from inside.
  Returning at the stripe node itself narrowed the join to 32 degrees and
  the wing opening to 4.83 (both metric failures), and a shallower lobe
  lost the droop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5d2f4a16-ffda-4c09-85d2-18b66770025f"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1808-bee-with-drooping-wings/bee-with-drooping-wings_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24             # mirror axis
HEAD_R = 5
HEAD_C = (AX, 9)    # head top on y=4; its bottom point is the abdomen apex
BODY_R = 6          # abdomen half-width: sides on x=18 and x=30
CAP_TOP_Y = 20      # top cap centre (apex y=14)
CAP_BOT_Y = 38      # bottom cap centre (apex y=44)
STRIPES = (24, 34)  # 10 from each apex, 10 apart
WING_W = (8, 36)    # outermost wing point (vertical tangent) on x=8
BOWL_R = 4          # wing bottom: arc about (12, 36) from WING_W to (12, 40)
OUTER = ((14, 26), (8, 30))   # outer flank controls: stripe-1 node -> WING_W
UNDER = ((15, 40), (17, 39))   # underside controls: bowl bottom -> cap joint


def mirror(p):
    return (2 * AX - p[0], p[1])


class BeeWithDroopingWingsRedraw(Solo48):
    icon_id = "bee-with-drooping-wings-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/insects"
    aliases = ("honeybee", "bumblebee")
    keywords = ("bee", "honeybee", "insect", "wings", "striped", "pollinator")

    def build(self) -> None:
        hx, hy = HEAD_C
        r = HEAD_R
        self.add_arc("head-nw", (hx - r, hy), (hx, hy - r), radius_x=r, sweep=True)
        self.add_arc("head-ne", (hx, hy - r), (hx + r, hy), radius_x=r, sweep=True)
        self.add_arc("head-se", (hx + r, hy), (hx, hy + r), radius_x=r, sweep=True)
        self.add_arc("head-sw", (hx, hy + r), (hx - r, hy), radius_x=r, sweep=True)
        self.add_contour("head", "head-nw", "head-ne", "head-se", "head-sw", closed=True)

        # Abdomen: a pill, clockwise from the apex; sides split at the stripes.
        L, R = AX - BODY_R, AX + BODY_R
        apex, bottom = (AX, CAP_TOP_Y - BODY_R), (AX, CAP_BOT_Y + BODY_R)
        s1, s2 = STRIPES
        self.add_arc("cap-top-r", apex, (R, CAP_TOP_Y), radius_x=BODY_R, sweep=True)
        self.add_line("side-r-1", (R, CAP_TOP_Y), (R, s1))
        self.add_line("side-r-2", (R, s1), (R, s2))
        self.add_line("side-r-3", (R, s2), (R, CAP_BOT_Y))
        self.add_arc("cap-bot-r", (R, CAP_BOT_Y), bottom, radius_x=BODY_R, sweep=True)
        self.add_arc("cap-bot-l", bottom, (L, CAP_BOT_Y), radius_x=BODY_R, sweep=True)
        self.add_line("side-l-3", (L, CAP_BOT_Y), (L, s2))
        self.add_line("side-l-2", (L, s2), (L, s1))
        self.add_line("side-l-1", (L, s1), (L, CAP_TOP_Y))
        self.add_arc("cap-top-l", (L, CAP_TOP_Y), apex, radius_x=BODY_R, sweep=True)
        self.add_contour("abdomen", "cap-top-r", "side-r-1", "side-r-2", "side-r-3",
                         "cap-bot-r", "cap-bot-l", "side-l-3", "side-l-2", "side-l-1",
                         "cap-top-l", closed=True)
        self.add_line("stripe-1", (L, s1), (R, s1))
        self.add_line("stripe-2", (L, s2), (R, s2))
        for stripe, above, below in (("stripe-1", 1, 2), ("stripe-2", 2, 3)):
            for side in "lr":
                self.relate("connect", stripe, f"side-{side}-{above}")
                self.relate("connect", stripe, f"side-{side}-{below}")
        self.relate("connect", "head-se", "cap-top-r")
        self.relate("connect", "head-sw", "cap-top-l")

        # Wings: a drooping lobe hung on each side of the abdomen, from the
        # upper stripe node out to x=8, round at the bottom, and back level
        # into the bottom cap joint. Built on the left and mirrored.
        wx, wy = WING_W
        low = (wx + BOWL_R, wy + BOWL_R)
        left = ((L, s1), WING_W, low, (L, CAP_BOT_Y), OUTER, UNDER)
        right = tuple(mirror(p) for p in left[:4]) + tuple(tuple(mirror(p) for p in c) for c in left[4:])
        for side, (root, far, lowest, ret, oc, uc) in (("l", left), ("r", right)):
            self.add_bezier(f"wing-{side}-outer", root, (oc[0], oc[1], far))
            self.add_arc(f"wing-{side}-bowl", far, lowest, radius_x=BOWL_R, sweep=(side == "r"))
            self.add_bezier(f"wing-{side}-under", lowest, (uc[0], uc[1], ret))
            self.add_contour(f"wing-{side}", f"wing-{side}-outer", f"wing-{side}-bowl",
                             f"wing-{side}-under")
            for member in (f"side-{side}-1", f"side-{side}-2", "stripe-1"):
                self.relate("connect", f"wing-{side}-outer", member)
            for member in (f"side-{side}-3", f"cap-bot-{side}"):
                self.relate("connect", f"wing-{side}-under", member)
