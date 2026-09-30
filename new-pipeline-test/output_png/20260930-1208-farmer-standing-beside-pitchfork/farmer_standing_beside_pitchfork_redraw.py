"""farmer-standing-beside-pitchfork (redraw of the new-pipeline traced SVG).

Plan: stick farmer left, upright three-tine pitchfork right, on SQUARE
(centerline box (6,6)-(42,42)).
- head: 4-cardinal-arc circle, r4, centre (FX,10); top touches y=6.
- torso: vertical line from the neck (FX,22) to the hip; the neck sits exactly
  8 centerline units under the head outline (4-unit ink gap, human-reference.md).
- arms: inverted V from the neck, hands 8 either side of the torso; the left
  hand is the x=6 extreme.
- legs: inverted V from the hip to the y=42 floor.
- pitchfork: middle tine + shaft on x=SX from y=6 to the y=42 floor, split at
  the U bottom; outer tines 8 either side (right tine = x=42 extreme), each
  turning into the shaft with an r8 quarter arc (Psi shape), standalone lines
  so the head-to-left-tine gap of exactly 8 certifies.
Keyshape: the metrics suggested VRECT_M (28 wide). A three-tine fork is 16
wide at 8 tine spacing, the head needs 8 of its own plus an 8 gap to the left
tine, and the free arm needs 8 of spread: 16 + 8 + 8 + 4 + 8 = 44 > 28 (VRECT_L
32 leaves the left arm only 4). SQUARE's 36 width fits it all.
Metric issues fixed: head-to-body clearance 3.09 -> exact 8 (e0/e5,e6,e7);
fork tine gaps 4.36/4.38 -> 8 (e1/e2, e2/e3); legs vs arms/torso 5.4-7.3 -> >=8
(e4 vs e5,e6,e7); arm-torso wedges 33 deg / 4.8 apart -> 45 deg arms whose hands
sit 8 from the torso; undersized head hole 3.31 -> r4 ring on the grid (the
human-reference head); stroke width 2.55 -> 4; 8 strokes -> 6 parts (head,
torso, arms, legs, fork, shaft); VRECT_M 96% y fill -> SQUARE, every extreme
exactly on its box.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No Lucide pitchfork; the fork follows the
Psi construction of the trace.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "82d178e5-3f74-432a-987e-abc1c9057ae8"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1208-farmer-standing-beside-pitchfork/"
    "farmer-standing-beside-pitchfork_raw.svg"
)
AUTHOR = "claude-opus-5-5"

FX = 14          # figure axis
HEAD_R = 4
HEAD_CY = 10
NECK = (FX, 22)  # HEAD_CY + HEAD_R + 8
HIP = (FX, 32)
HANDS = ((FX - 8, 29), (FX + 8, 29))
FEET = ((FX - 6, 42), (FX + 6, 42))
SX = 34          # pitchfork shaft axis
TINE = 8         # tine spacing = U radius
TOP, FLOOR = 6, 42
TINE_BASE = 14   # where the outer tines turn into the U
U_BOTTOM = (SX, TINE_BASE + TINE)


class FarmerStandingBesidePitchforkRedraw(Solo48):
    icon_id = "farmer-standing-beside-pitchfork-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/occupations"
    aliases = ("farmer", "farmer with pitchfork")
    keywords = ("farmer", "pitchfork", "farm", "agriculture", "harvest", "hay", "person")

    def build(self) -> None:
        cx, cy, r = FX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("farmer", head="head", torso="torso", torso_junction="start")

        self.add_line("left-arm", NECK, HANDS[0])
        self.add_line("right-arm", NECK, HANDS[1])
        self.relate("connect", "left-arm", "torso")
        self.relate("connect", "right-arm", "torso")
        self.relate("connect", "left-arm", "right-arm")

        self.add_line("left-leg", HIP, FEET[0])
        self.add_line("right-leg", HIP, FEET[1])
        self.relate("connect", "left-leg", "torso")
        self.relate("connect", "right-leg", "torso")
        self.relate("connect", "left-leg", "right-leg")

        lx, rx = SX - TINE, SX + TINE
        self.add_line("left-tine", (lx, TOP), (lx, TINE_BASE))
        self.add_line("right-tine", (rx, TOP), (rx, TINE_BASE))
        self.add_arc("fork-left", (lx, TINE_BASE), U_BOTTOM, radius_x=TINE, sweep=False)
        self.add_arc("fork-right", U_BOTTOM, (rx, TINE_BASE), radius_x=TINE, sweep=False)
        self.add_contour("fork", "fork-left", "fork-right")
        self.relate("connect", "left-tine", "fork")
        self.relate("connect", "right-tine", "fork")

        self.add_line("middle-tine", (SX, TOP), U_BOTTOM)
        self.add_line("shaft", U_BOTTOM, (SX, FLOOR))
        self.relate("connect", "middle-tine", "fork")
        self.relate("connect", "shaft", "fork")
        self.relate("connect", "middle-tine", "shaft")
