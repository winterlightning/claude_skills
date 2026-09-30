"""gift-heart (redraw of the new-pipeline traced SVG).

Subject: a gift box with a hollow heart floating above its lid.

Plan: VRECT_L (centerline box (8,4)-(40,44)), mirrored about x=24.
- heart: one closed cubic run, lobes top at y=4 and out to x=15/33, a V tip at
  (24,17) and a shallow notch cusp at (24,7) (a deeper notch ran parallel to
  the lower sides closer than 8 and failed the internal-spacing gate).
- lid: closed rectangle (8,25)-(40,33), the full keyshape width; its bottom
  edge is split at x=11/24/37 where the body and ribbon attach.
- body: open U (11,33)-(11,44)-(37,44)-(37,33) hanging from the lid, so the
  lid overhangs by 3 each side; the ribbon runs (24,33)-(24,44) and splits it.
Vertical budget: heart 13 + gap 8 + lid 8 + body 11 = 40.

Keyshape: metrics suggested SQUARE, but it fills only 86% on x (stretch 1.16),
while VRECT_L needs the smaller stretch (1.08 on y) and gives the 40-unit
height the heart, gap, lid and body need at stroke 4. SQUARE's 36 left the
body under 10 tall.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (warn): all four extremes sit on the VRECT_L box (lid
  x=8/40, heart top y=4, body bottom y=44).
- clearance e0/e3 3.66 (error): heart tip to lid top is now 8 on centerlines.
- hole at the heart 5.0 (error): heart widened to 18x13 so its eye clears the
  hole minimum.
- hole 0.8 at the lid's left end (error): the trace's lid-overhang sliver is
  gone; the lid is one clean rectangle with an 8-tall eye, and the body hangs
  from its bottom edge.
Lucide `gift` informed the lid-and-body box; Lucide `heart` the lobes and V tip.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5862a2a1-e7c8-522a-812d-2db80570e593"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1255-gift-heart/gift-heart_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEART_TOP, HEART_NOTCH, HEART_TIP = 4, 7, 17
LOBE_Y = 8                               # lobe extreme height
LOBE_TOP_X, LOBE_OUT_X = 19, 15          # left lobe apex x / left extreme x
LID_L, LID_R, LID_T, LID_B = 8, 40, 25, 33
BODY_L, BODY_R, BODY_B = 11, 37, 44
K = 0.5523                              # quarter-ellipse handle ratio


def mx(p):
    return (2 * AXIS - p[0], p[1])


class GiftHeartRedraw(Solo48):
    icon_id = "gift-heart-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/award"
    aliases = ("gift with heart", "love gift", "present with heart")
    keywords = ("gift", "present", "box", "heart", "love", "valentine", "donation")

    def build(self) -> None:
        # Heart: notch -> left lobe apex -> left extreme -> tip, then mirrored back.
        notch, tip = (AXIS, HEART_NOTCH), (AXIS, HEART_TIP)
        apex, out = (LOBE_TOP_X, HEART_TOP), (LOBE_OUT_X, LOBE_Y)
        rx, ry = LOBE_TOP_X - LOBE_OUT_X, LOBE_Y - HEART_TOP
        left = [
            ((23.5, 5), (21.5, HEART_TOP), apex),
            ((apex[0] - rx * K, HEART_TOP), (LOBE_OUT_X, LOBE_Y - ry * K), out),
            ((LOBE_OUT_X, 11), (20.5, 14), tip),
        ]
        # Right half runs tip -> notch: mirror the left run and reverse it.
        right = []
        pts = [notch] + [s[2] for s in left]
        for i in range(len(left) - 1, -1, -1):
            c1, c2, _ = left[i]
            right.append((mx(c2), mx(c1), mx(pts[i])))
        self.add_bezier("heart-l", notch, *left)
        self.add_bezier("heart-r", tip, *right)
        self.add_contour("heart", "heart-l", "heart-r", closed=True)

        # Lid: closed rectangle, bottom edge split where body walls and ribbon attach.
        self.add_polyline(
            "lid",
            (LID_L, LID_T), (LID_R, LID_T), (LID_R, LID_B),
            (BODY_R, LID_B), (AXIS, LID_B), (BODY_L, LID_B), (LID_L, LID_B),
            closed=True,
        )
        # Body: open U hanging from the lid, bottom split at the ribbon.
        self.add_polyline(
            "body",
            (BODY_L, LID_B), (BODY_L, BODY_B), (AXIS, BODY_B), (BODY_R, BODY_B), (BODY_R, LID_B),
        )
        self.add_line("ribbon", (AXIS, LID_B), (AXIS, BODY_B))
        self.relate("connect", "body", "lid")
        self.relate("connect", "ribbon", "lid")
        self.relate("connect", "ribbon", "body")
