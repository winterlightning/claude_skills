"""grim-reaper-with-scythe (redraw of the new-pipeline traced SVG).

Plan: stick figure left, tall scythe right, on SQUARE (centerline box (6,6)-(42,42)).
- head: 4-cardinal-arc circle, r4, centre (FX,10); top touches y=6.
- torso: vertical line from the neck (FX,22) to the hip; the neck sits exactly
  8 centerline units under the head outline (4-unit ink gap, human-reference.md).
- arms leave the neck like the reference: the free arm hangs down-left to the
  x=6 extreme, the other arm reaches right and grips the shaft (shaft split at
  the hand, shared endpoint) instead of stopping short of it.
- legs: inverted V from the hip to the y=42 floor.
- scythe: vertical shaft x=SX (the traced shaft leaned 8 degrees; upright keeps
  it 8 clear of the front foot). Closed crescent blade: outer arc r13 about
  (SX,19) from the shaft top through the x=42 extreme down to the tip (41,24)
  (5-12-13 point), inner arc r14 back to the shaft at y=16, so the tip hangs
  down like a scythe rather than reading as a flag or a cane hook.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide match for a scythe.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1437-grim-reaper-with-scythe/"
    "grim-reaper-with-scythe_raw.svg"
)
AUTHOR = "claude-opus-5-5"

FX = 15          # figure axis
HEAD_R = 4
HEAD_CY = 10
NECK = (FX, 22)  # HEAD_CY + HEAD_R + 8
HIP = (FX, 32)
FREE_HAND = (6, 29)
FEET = ((9, 42), (21, 42))
SX = 29          # shaft axis
SHAFT_TOP, SHAFT_BOTTOM = (SX, 6), (SX, 42)
GRIP = (SX, 26)
BLADE_R = 13     # outer edge, centre (SX, 19)
BLADE_EDGE = (SX + BLADE_R, 19)
BLADE_TIP = (SX + 12, 19 + 5)
BLADE_ROOT = (SX, 16)
BLADE_INNER_R = 14


class GrimReaperWithScytheRedraw(Solo48):
    icon_id = "grim-reaper-with-scythe-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("reaper", "death with scythe")
    keywords = ("grim reaper", "reaper", "scythe", "death", "halloween", "harvest")

    def build(self) -> None:
        cx, cy, r = FX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("reaper", head="head", torso="torso", torso_junction="start")

        self.add_line("free-arm", NECK, FREE_HAND)
        self.add_line("grip-arm", NECK, GRIP)
        self.relate("connect", "free-arm", "torso")
        self.relate("connect", "grip-arm", "torso")
        self.relate("connect", "free-arm", "grip-arm")

        self.add_line("rear-leg", HIP, FEET[0])
        self.add_line("front-leg", HIP, FEET[1])
        self.relate("connect", "rear-leg", "torso")
        self.relate("connect", "front-leg", "torso")
        self.relate("connect", "rear-leg", "front-leg")

        self.add_arc("blade-outer-1", SHAFT_TOP, BLADE_EDGE, radius_x=BLADE_R, sweep=True)
        self.add_arc("blade-outer-2", BLADE_EDGE, BLADE_TIP, radius_x=BLADE_R, sweep=True)
        self.add_arc("blade-inner", BLADE_TIP, BLADE_ROOT, radius_x=BLADE_INNER_R, sweep=False)
        self.add_line("blade-root", BLADE_ROOT, SHAFT_TOP)
        self.add_contour(
            "blade", "blade-outer-1", "blade-outer-2", "blade-inner", "blade-root", closed=True,
        )

        self.add_line("shaft-top", BLADE_ROOT, GRIP)
        self.add_line("shaft-bottom", GRIP, SHAFT_BOTTOM)
        self.add_contour("shaft", "shaft-top", "shaft-bottom")
        self.relate("connect", "shaft", "blade")
        self.relate("connect", "shaft", "grip-arm")
