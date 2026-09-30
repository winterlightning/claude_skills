"""graduate-with-two-people (redraw of the new-pipeline traced SVG).

Plan: three head-and-shoulders busts in a row, the centre one wearing a
mortarboard, on HRECT_L (centerline box (4,8)-(44,40)); mirrored about x=24.
- cap: closed kite-diamond board, top vertex on the y=8 extreme, corners at
  (15,13)/(33,13), bottom vertex (24,19) = the graduate's head top (shared
  node, declared connect), so the board sits on the head as in the image.
  10 tall so its opposite edges keep 8 on centerlines.
- heads: 4-cardinal-arc circles r4 on one row y=23, centres 16 apart
  (8 between outlines); side heads touch the x=4/44 extremes and clear the
  cap corners by 8.2.
- shoulders: one open contour of six cubics, an arch per person: outer ends
  vertical on the bottom extreme (4,40)/(44,40), a horizontal apex exactly
  8 under each head outline (4-unit ink gap, human-reference.md), and steep
  cusps on the bottom edge at (16,40)/(32,40) between the arches.
References: icon_set/references/human_ref/user.svg (circular head, broad open
shoulder arch, head-to-shoulder gap); Lucide `users` / `graduation-cap`
(repeated busts, flat diamond board).

Metric issues:
- clearance e0/e1 (cap legs) vs heads e3/e4/e5: fixed, the two cap legs are
  dropped; the board now rests on the head tip instead.
- stroke-count 7 > 6: fixed, 5 strokes (cap, three heads, shoulders).
- clearance e2 (cap) vs e3/e5 (side heads): fixed, 8.2 on centerlines.
- clearance/head-gap e2 vs e4: fixed, deliberate shared node + connect
  (cap on head); the head's body gap is certified against its shoulders.
- clearance e3/e4, e4/e5 (head to head): fixed, 8 between outlines.
- clearance e3/e4/e5 vs e6 (heads vs shoulders): fixed, exactly 8 on
  centerlines at every lobe apex.
- keyshape-short-axis: fixed by moving to HRECT_L (score 0.82 vs 0.90):
  cap 10 + head 8 + gap 8 + shoulders 5 needs 32 rows, HRECT_M has 28.
  Every extreme lands on its box (cap top y=8, arch ends y=40, x=4/44).
- stroke-width: fixed, stroke 4 throughout.
- holes: build-gate sizes pass, but the pipeline's 6-ink target is NOT met:
  head holes are 4 ink wide (r4) and the cap hole under 6. r5 heads need 18
  between centres (x=6..42 puts outlines past the 4..44 box), and a
  6-ink diamond hole needs a 12-tall board, which leaves no height for the
  shoulders on any keyshape.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3bbdfa95-8a10-4cf0-910a-fb693fb29316"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1307-graduate-with-two-people/"
    "graduate-with-two-people_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_R = 4
CENTRE_HEAD = (AXIS, 23)
SIDE_DX = 16                 # head centre spacing: 2r + 8
SIDE_HEAD_Y = 23
GAP = 8                      # head outline -> shoulder apex, centerlines
CAP_TOP, CAP_W = 8, 9       # board: top vertex y, half-width
CAP_UP, CAP_DOWN = 5, 6      # corner drop below the top, bottom drop below the corners
BOTTOM = 40
EDGE = 4                     # left extreme; right is 48 - EDGE
CUSP = (16, 40)              # left cusp on the bottom edge; right one mirrored
K = 0.5523                   # quarter-ellipse cubic factor


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class GraduateWithTwoPeopleRedraw(Solo48):
    icon_id = "graduate-with-two-people-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/education"
    aliases = ("graduate group", "graduation class", "students")
    keywords = ("graduate", "graduation", "mortarboard", "students", "people",
                "group", "education", "alumni", "family")

    def head(self, name: str, c: tuple[int, int]) -> None:
        cx, cy, r = c[0], c[1], HEAD_R
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4",
                         closed=True)

    def build(self) -> None:
        left_head = (AXIS - SIDE_DX, SIDE_HEAD_Y)
        right_head = mirror(left_head)
        self.head("head-left", left_head)
        self.head("head-centre", CENTRE_HEAD)
        self.head("head-right", right_head)

        # Mortarboard: top, right, bottom (= centre head top), left.
        corner_y = CAP_TOP + CAP_UP
        cap_bottom = (AXIS, corner_y + CAP_DOWN)
        assert cap_bottom == (CENTRE_HEAD[0], CENTRE_HEAD[1] - HEAD_R)
        self.add_polyline("cap", (AXIS, CAP_TOP), (AXIS + CAP_W, corner_y),
                          cap_bottom, (AXIS - CAP_W, corner_y), closed=True)
        self.relate("connect", "cap", "head-centre")

        # Shoulders: apexes 8 under each head outline.
        side_apex = (left_head[0], left_head[1] + HEAD_R + GAP)       # (8,35)
        centre_apex = (AXIS, CENTRE_HEAD[1] + HEAD_R + GAP)          # (24,35)
        outer = (EDGE, BOTTOM)
        cx, cy = CUSP
        # outer end -> side apex: quarter ellipse, vertical then horizontal.
        w, h = side_apex[0] - outer[0], outer[1] - side_apex[1]
        seg_outer = ((outer[0], outer[1] - K * h), (side_apex[0] - K * w, side_apex[1]),
                     side_apex)
        # side apex -> cusp: leave horizontal, arrive steeply (about 60 deg).
        seg_inner = ((side_apex[0] + 4.4, side_apex[1]), (cx - 1.5, cy - 2.6), CUSP)
        # cusp -> centre apex: the mirror image of seg_inner about x=16.
        seg_mid = ((cx + 1.5, cy - 2.6), (centre_apex[0] - 4.4, centre_apex[1]),
                   centre_apex)

        def rev(start, seg):
            """Mirror a cubic about the axis and walk it backwards."""
            c1, c2, end = seg
            return mirror(end), (mirror(c2), mirror(c1), mirror(start))

        self.add_bezier("body-left-outer", outer, seg_outer)
        self.add_bezier("body-left-inner", side_apex, seg_inner)
        self.add_bezier("body-centre-left", CUSP, seg_mid)
        s, seg = rev(CUSP, seg_mid)
        self.add_bezier("body-centre-right", s, seg)
        s, seg = rev(side_apex, seg_inner)
        self.add_bezier("body-right-inner", s, seg)
        s, seg = rev(outer, seg_outer)
        self.add_bezier("body-right-outer", s, seg)
        self.add_contour("shoulders", "body-left-outer", "body-left-inner",
                         "body-centre-left", "body-centre-right",
                         "body-right-inner", "body-right-outer")

        self.mark_human_figure("person-left", head="head-left",
                               torso="body-left-outer", torso_junction="end")
        self.mark_human_figure("graduate", head="head-centre",
                               torso="body-centre-left", torso_junction="end")
        self.mark_human_figure("person-right", head="head-right",
                               torso="body-right-outer", torso_junction="start")
