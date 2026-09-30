"""genie (redraw of the new-pipeline traced SVG).

Plan (VRECT_M, centerline box (10,4)-(38,44)):
- Head: full circle of four cardinal quarter arcs, r5 about (24,9); top = 4.
- Neck: standalone vertical torso line (24,22)-(24,26), exactly 8 below the
  head outline (certified head gap: head straight above an axis-aligned neck).
- Arms: one contour of two mirrored cubics branching from the torso base
  (24,26), sweeping out and up to raised hands at (12,16) / (36,16).
- Smoke tail: one S cubic from the torso base down into the lamp rim (16,34).
- Lamp: rim line split at the smoke junction, a r10 semicircular bowl about
  (20,34) (left 10, bottom 44) and a spout cubic rising from the rim to its
  tip at (38,30).

Metric issues fixed:
- stroke-width (2.65): redrawn at stroke 4.
- keyshape-short-axis (x 66%): bowl reaches x=10 and the spout tip x=38.
- clearance e0/e1, e0/e2, e0/e3, e1/e2, e1/e3, e2/e3 (head, arms, torso
  crowding): arms now branch from the torso below the neck and their hands
  are >= 8.9 from the head outline; the head/neck gap is exactly 8.
- clearance e3/e4 (smoke to lamp 5.21): the 40-unit height cannot hold head
  (10) + gap (8) + body + gap (8) + a bowl deep enough for a 6-wide hole
  (10), so the smoke now issues from the lamp rim (genie rising out of the
  lamp) instead of floating 8 above it.
- hole at the head (1.22): head r5 leaves a 6-wide opening.
- hole in the lamp (1.4): bowl is 10 deep, a 6-wide opening.
- no-head: the head is a real circle, flagged with mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f9d2a78b-2eb0-40a5-bcec-c567992dd9f2"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1322-genie/genie_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24                    # figure axis
HEAD_CY, HEAD_R = 9, 5       # head circle; top on the keyshape edge y=4
NECK = (AXIS, 22)            # head bottom 14 + 8
HIP = (AXIS, 26)             # arms and smoke branch here
HAND_DX, HAND_Y = 12, 16     # raised hands at AXIS -/+ 12
RIM_Y, BOWL_CX, BOWL_R = 34, 20, 10
SMOKE_END = (16, RIM_Y)      # left of the bowl centre so the tail reads as an S
SPOUT_TIP = (38, 30)


class GenieRedraw(Solo48):
    icon_id = "genie-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/fantasy"
    aliases = ("genie", "genie-lamp", "magic-lamp")
    keywords = ("genie", "djinn", "lamp", "magic", "wish", "smoke", "fantasy", "arabian")

    def build(self) -> None:
        cx, cy, r = AXIS, HEAD_CY, HEAD_R
        self.add_arc("head-tr", (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc("head-br", (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc("head-bl", (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_arc("head-tl", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_contour("head", "head-tr", "head-br", "head-bl", "head-tl", closed=True)

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("genie", head="head", torso="torso", torso_junction="start")

        hx, hy = HIP
        self.add_bezier("arm-l", (AXIS - HAND_DX, HAND_Y),
                        ((AXIS - HAND_DX, 22), (AXIS - 8, hy), HIP))
        self.add_bezier("arm-r", HIP,
                        ((AXIS + 8, hy), (AXIS + HAND_DX, 22), (AXIS + HAND_DX, HAND_Y)))
        self.add_contour("arms", "arm-l", "arm-r")

        self.add_bezier("smoke", HIP, ((hx, 32), (SMOKE_END[0], 28), SMOKE_END))

        left, right = BOWL_CX - BOWL_R, BOWL_CX + BOWL_R
        self.add_line("rim-l", (left, RIM_Y), SMOKE_END)
        self.add_line("rim-r", SMOKE_END, (right, RIM_Y))
        self.add_arc("bowl", (right, RIM_Y), (left, RIM_Y), radius_x=BOWL_R)
        self.add_contour("lamp", "rim-l", "rim-r", "bowl", closed=True)
        self.add_bezier("spout", (right, RIM_Y), ((34, RIM_Y), (36, 33), SPOUT_TIP))

        self.relate("connect", "torso", "arms")
        self.relate("connect", "torso", "smoke")
        self.relate("connect", "arms", "smoke")
        self.relate("connect", "smoke", "lamp")
        self.relate("connect", "lamp", "spout")
