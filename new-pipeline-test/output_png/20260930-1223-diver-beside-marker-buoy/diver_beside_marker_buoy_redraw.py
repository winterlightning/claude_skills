"""diver-beside-marker-buoy (redraw of the new-pipeline traced SVG).

Subject: a stick-figure diver with fins swimming right along the bottom,
beside a tall capsule marker buoy on a short tether.

Plan on SQUARE (the metrics suggestion; centerline box (6,6)-(42,42)):
- buoy: capsule 10 wide (r5 caps about (11,11) and (11,17)); left wall on
  x=6 and top apex on y=6. The bottom cap is split at its apex (11,22) where
  the tether hangs to (11,27).
- diver: level torso on y=38 from the hip (14,38) to the neck (26,38),
  split at the shoulder (20,38); head ring r4 level beside the neck at
  (38,38) (12 from the neck = 8 on centerlines, 4 ink). The head sets the
  right edge x=42 and the bottom y=42.
- arm: one stroking arm from the shoulder up over the head, elbow (26,28),
  hand (34,26), 12.6 from the head centre.
- legs: two straight legs splayed from the hip at +/-26.6 degrees to
  (6,34) and (6,42), the fin kick; the lower one also touches y=42.

Deliberate changes from the image: the image's diagonal dive (head
lower-right, fins up-left, buoy upper-right) was redrawn first. At 8
spacing its head had to sit right under the tether and shrink to r2, and
it read as "!" beside a branch, not a person (also tried head-down and
hand-on-tether poses). A level swimmer with the buoy upper-left reads as
a diver at 48 px.

Metric issues:
- clearance e0/e5, e3/e5, e4/e5 (tether and arms against the head) ->
  fixed: the tether is 27+ from the head and the arm clears it by 8.6 ink
  gap on centerlines (12.6 from the centre).
- clearance e2/e3, e2/e4, e3/e4 (legs and arms crowding the torso) -> fixed:
  legs meet only at the shared hip node (53 degrees apart); the arm leaves
  the shoulder at 59 degrees.
- hole (buoy 2.2 inscribed, need 6) -> fixed: capsule 10 wide on
  centerlines, 6 ink inside.
- narrow-join warnings (30-42 degrees) -> fixed by the wider joins above.
- keyshape-short-axis (y 99%) -> fixed: extremes land exactly on 6/42.
- stroke-width (info) -> redrawn at stroke 4 with every gap budgeted at 8.
- human head gap (the trace had no detectable head) -> exactly 8 on
  centerlines, level head beside a level neck.
Not kept: the second arm (no room to reach forward past the head at 8
spacing) and the knee bends (the tether end sits over the legs).
Reference: icon_set/references/human_ref (stick figure, detached ring head
on the torso axis) and Lucide person-standing limbs. No Lucide buoy; the
capsule follows Lucide's pill construction (semicircle caps tangent to
straight sides).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "05eae23b-b81d-5ba9-a08b-414daf65ebe4"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1223-diver-beside-marker-buoy/"
    "diver-beside-marker-buoy_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# buoy
BX, BR = 11, 5            # capsule axis and cap radius
B_TOP, B_BOT = 11, 17     # cap centres
TETHER_END = (BX, 27)
# diver
BODY_Y = 38
HIP, SHOULDER, NECK = (14, BODY_Y), (20, BODY_Y), (26, BODY_Y)
HEAD_R = 4
HEAD = (NECK[0] + 12, BODY_Y)   # centre 12 from the neck: 8 on centerlines
ELBOW, HAND = (26, 28), (34, 26)
KICK = 4                  # legs splay +/-KICK about the body line
FOOT_X = 6


class DiverBesideMarkerBuoyRedraw(Solo48):
    icon_id = "diver-beside-marker-buoy-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation/diving"
    aliases = ("scuba diver with buoy", "diver and marker buoy")
    keywords = ("diver", "diving", "scuba", "buoy", "marker", "surface marker", "underwater")

    def build(self) -> None:
        # marker buoy: capsule split at the bottom apex for the tether
        left, right = BX - BR, BX + BR
        self.add_arc("buoy-top", (left, B_TOP), (right, B_TOP), radius_x=BR)
        self.add_line("buoy-right", (right, B_TOP), (right, B_BOT))
        self.add_arc("buoy-bottom-right", (right, B_BOT), (BX, B_BOT + BR), radius_x=BR)
        self.add_arc("buoy-bottom-left", (BX, B_BOT + BR), (left, B_BOT), radius_x=BR)
        self.add_line("buoy-left", (left, B_BOT), (left, B_TOP))
        self.add_contour(
            "buoy", "buoy-top", "buoy-right", "buoy-bottom-right",
            "buoy-bottom-left", "buoy-left", closed=True,
        )
        self.add_line("tether", (BX, B_BOT + BR), TETHER_END)
        self.relate("connect", "tether", "buoy")

        # diver: level body, head level beside the neck
        hx, hy = HEAD
        self.add_arc("head-top", (hx - HEAD_R, hy), (hx + HEAD_R, hy), radius_x=HEAD_R)
        self.add_arc("head-bottom", (hx + HEAD_R, hy), (hx - HEAD_R, hy), radius_x=HEAD_R)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_line("torso-low", HIP, SHOULDER)
        self.add_line("torso", SHOULDER, NECK)
        self.add_contour("body", "torso-low", "torso")
        self.mark_human_figure("diver", head="head", torso="torso", torso_junction="end")

        self.add_polyline("arm", SHOULDER, ELBOW, HAND)
        self.relate("connect", "arm", "body")

        # fin kick: two legs mirrored about the body line
        self.add_line("leg-up", HIP, (FOOT_X, BODY_Y - KICK))
        self.add_line("leg-down", HIP, (FOOT_X, BODY_Y + KICK))
        for leg in ("leg-up", "leg-down"):
            self.relate("connect", leg, "body")
        self.relate("connect", "leg-up", "leg-down")
