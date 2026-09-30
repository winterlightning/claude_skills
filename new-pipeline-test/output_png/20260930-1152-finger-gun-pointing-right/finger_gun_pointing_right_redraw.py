"""finger gun pointing right (redraw of the new-pipeline traced SVG).

Plan: one right hand in side view on HRECT_M (centerline box (4,10)-(44,38)).
- outline: one closed contour. The upright thumb is a tube of width 8 (x 16..24)
  with a radius-4 tip whose apex is the y=10 extreme; the index finger is a
  horizontal tube of width 8 (y 20..28) with a radius-4 tip whose apex is the
  x=44 extreme; the curled fingers bulge out under the index finger as a
  radius-5 half round; the palm is a flat bottom (the y=38 extreme) turning up
  through a radius-8 heel into the cut wrist edge on x=4. The thumb's back runs
  down into the wrist corner as one smooth cubic.
- curl: the three curled fingers are merged into one rounded finger (a pill
  from x 19 to 37) whose top edge carries on from the index finger's underside
  and whose rounded left end meets the palm bottom tangentially. Both ends share
  outline nodes and are declared with relate("connect").
Metric issues fixed:
- clearance x7 (e1/e3, e1/e5, e2/e4, e2/e5, e2/e6, e3/e5, e3/e6 at 3.2..7.4
  centerline): the three stacked finger pills cannot fit at stroke 4 inside a
  28-unit short axis (three pills plus the index finger need 4 x 8 + walls), so
  they are merged into one curled finger; every remaining gap is >= 8.
- hole x3 (0.2..0.8 inscribed slivers between the finger pills): gone with the
  merge; the curled finger encloses a 10-unit (centerline) opening.
- stroke-count (7, budget 6): two elements, the outline and the curl.
- narrow-join (e0/e2 21 deg wedge at the wrist) and loose-join x4: the wrist is
  a single 90-degree corner of the outline; every contact is a shared node.
- keyshape-short-axis (x filled 96%): the extremes sit exactly on x 4 and 44,
  y 10 and 38.
- stroke-width (2.55 in the trace): drawn at the profile stroke 4.
No sideways pointing hand in Lucide; construction follows Lucide's
tube-and-round-cap finger style (hand, pointer).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3b465551-d19d-4922-ba95-a345098fba79"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1152-finger-gun-pointing-right/finger-gun-pointing-right_raw.svg"
AUTHOR = "claude-opus-5-5"

FINGER_W = 8                    # tube width of thumb and index finger
TIP_R = FINGER_W // 2
THUMB_X = (16, 24)              # thumb tube, tip apex on y=10
INDEX_Y = (20, 28)              # index tube, tip apex on x=44
WRIST_X, WRIST_TOP = 4, 24
BOTTOM_Y = 38
HEEL_R = 8
CURL_R = (BOTTOM_Y - INDEX_Y[1]) // 2   # 5: curled finger half rounds
CURL_FRONT_X = 32
CURL_BACK_X = 24


class FingerGunPointingRightRedraw(Solo48):
    icon_id = "finger-gun-pointing-right-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    aliases = ("finger gun", "pointing hand", "hand pointing right")
    keywords = ("hand", "finger", "gun", "pointing", "right", "gesture", "direction")

    def build(self) -> None:
        tl, tr = THUMB_X
        it, ib = INDEX_Y
        thumb_base = TIP_R + 10              # y where the thumb tip arc ends
        tip_x = 44 - TIP_R
        heel = (WRIST_X + HEEL_R, BOTTOM_Y)

        self.add_arc("thumb-tip", (tl, thumb_base), (tr, thumb_base), radius_x=TIP_R)
        self.add_line("thumb-front", (tr, thumb_base), (tr, it))
        self.add_line("index-top", (tr, it), (tip_x, it))
        self.add_arc("index-tip", (tip_x, it), (tip_x, ib), radius_x=TIP_R)
        self.add_line("index-under", (tip_x, ib), (CURL_FRONT_X, ib))
        self.add_arc("curl-front", (CURL_FRONT_X, ib), (CURL_FRONT_X, BOTTOM_Y), radius_x=CURL_R)
        self.add_line("bottom-front", (CURL_FRONT_X, BOTTOM_Y), (CURL_BACK_X, BOTTOM_Y))
        self.add_line("bottom-back", (CURL_BACK_X, BOTTOM_Y), heel)
        self.add_arc("heel", heel, (WRIST_X, BOTTOM_Y - HEEL_R), radius_x=HEEL_R)
        self.add_line("wrist", (WRIST_X, BOTTOM_Y - HEEL_R), (WRIST_X, WRIST_TOP))
        self.add_bezier("thumb-back", (WRIST_X, WRIST_TOP),
                        ((10, WRIST_TOP), (tl, 20), (tl, thumb_base)))
        self.add_contour("outline", "thumb-tip", "thumb-front", "index-top", "index-tip",
                         "index-under", "curl-front", "bottom-front", "bottom-back",
                         "heel", "wrist", "thumb-back", closed=True)

        self.add_line("curl-top", (CURL_FRONT_X, ib), (CURL_BACK_X, ib))
        self.add_arc("curl-back", (CURL_BACK_X, ib), (CURL_BACK_X, BOTTOM_Y),
                     radius_x=CURL_R, sweep=False)
        self.add_contour("curl", "curl-top", "curl-back")
        self.relate("connect", "curl", "outline")
