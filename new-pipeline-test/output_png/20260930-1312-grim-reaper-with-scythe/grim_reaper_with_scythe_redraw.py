"""grim-reaper-with-scythe (redraw of the new-pipeline traced SVG).

Plan: stick figure under a tall scythe, on VRECT_M (centerline box (10,4)-(38,44)),
the keyshape the metrics suggested (score 0.91, tall hint).
- scythe: one contour. The blade is a single arc r53 about (38,57) (28-45-53
  triple) from the tip (10,12) up to the shaft top (38,4), its apex, so the
  blade sets the x=10 and y=4 extremes without overshoot; the shaft runs down
  x=38 to y=44 and is split at the grip.
- head: 4-cardinal-arc circle r4 about (24,19); 8.5 clear of the blade arc and
  10.4 clear of the blade tip.
- torso: vertical from the neck (24,31) to the hip (24,36); the neck is exactly
  8 centerline units below the head outline (4-unit ink gap, human-reference.md).
- arm: one horizontal arm from the neck to the shaft grip (38,31), sharing the
  shaft split point.
- legs: inverted V from the hip to (18,44) and (30,44) (3-4-5 slopes); the front
  foot is 8 clear of the shaft.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: blade tip on x=10, shaft on x=38, blade apex y=4, feet
  and shaft foot y=44 -- all four VRECT_M extremes exact.
- clearance e0/e2 (shaft vs front leg at the floor): front foot moved to x=30.
- clearance e0/e4 (blade vs head): head dropped under the blade, 8.5 clear.
- clearance e1/e2 (legs pinched near the feet): legs are one inverted V from a
  shared hip, feet 12 apart.
- clearance e1/e3, e2/e3 (second arm crowding the leg and first arm at the
  shaft): the second arm is dropped; one arm grips the shaft.
- clearance e2/e4, e3/e4 and head-gap: head centred on the torso axis with
  exactly 8 centerline / 4 ink from the neck; the arm leaves at the neck,
  12 below the head centre.
- holes (blade crescent pinch 0.63, arm/shaft pocket 5.0, head interior 2.16):
  the blade is an open arc (no crescent pocket), the single arm leaves no
  pocket. Head interior only partly fixed: r4 leaves 4 inscribed (was 2.16,
  target 6). r5 would reach 6, but under the blade it pushes the neck to y=33
  and shrinks the torso to 4 units, which reads worse at 48 px. The validator
  and build_gate.py both pass the r4 head.

Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide match for a scythe.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "10802c86-44a5-43d2-9258-49fbaaa0c39d"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1312-grim-reaper-with-scythe/"
    "grim-reaper-with-scythe_raw.svg"
)
AUTHOR = "claude-opus-5-5"

FX = 24                    # figure axis
HEAD_R = 4
HEAD_CY = 19
NECK = (FX, HEAD_CY + HEAD_R + 8)
HIP = (FX, 36)
FEET = ((FX - 6, 44), (FX + 6, 44))
SX = 38                    # shaft axis
SHAFT_TOP, SHAFT_BOTTOM = (SX, 4), (SX, 44)
GRIP = (SX, NECK[1])
BLADE_R = 53               # centre (SX, 57)
BLADE_TIP = (10, 12)


class GrimReaperWithScytheRedraw(Solo48):
    icon_id = "grim-reaper-with-scythe-redraw"
    keyshape = Keyshape.VRECT_M
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

        self.add_line("arm", NECK, GRIP)
        self.relate("connect", "arm", "torso")

        self.add_line("rear-leg", HIP, FEET[0])
        self.add_line("front-leg", HIP, FEET[1])
        self.relate("connect", "rear-leg", "torso")
        self.relate("connect", "front-leg", "torso")
        self.relate("connect", "rear-leg", "front-leg")

        self.add_arc("blade", BLADE_TIP, SHAFT_TOP, radius_x=BLADE_R, sweep=True)
        self.add_line("shaft-top", SHAFT_TOP, GRIP)
        self.add_line("shaft-bottom", GRIP, SHAFT_BOTTOM)
        self.add_contour("scythe", "blade", "shaft-top", "shaft-bottom")
        self.relate("connect", "scythe", "arm")
