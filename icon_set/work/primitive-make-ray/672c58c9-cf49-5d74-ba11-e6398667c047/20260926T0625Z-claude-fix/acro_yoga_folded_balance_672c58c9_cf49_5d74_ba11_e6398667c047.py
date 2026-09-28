"""Acro yoga folded balance: a flyer folded over the raised arm of a base partner who
lies on the ground with legs hooked up.

Symbol plan (reviewer feedback, point by point):
- Upper section (the flyer): one stroke with a rounded top - a radius-5 arc over
  the spine at x=24 - and two left-facing extensions: a straight limb down-left
  from the top to the left edge, and a horizontal limb left from the spine foot.
- Curved side detail: a radius-6 half disc bulging right from the spine, replacing
  the rejected upper-right circle.
- Gap: the lower section starts exactly 8 below the upper section's foot on the
  same vertical axis (4 units ink edge to edge).
- Lower section (the base): one bent stroke - the raised arm down to the ground
  line, the lying torso along y=40, and a rounded upward hook (radius-4 arc and a
  short rise) on the right.
- The base's separate head ring (radius 4) sits on the torso axis, 8 centerline
  (4 ink) beyond the neck junction (24,40), per the shared human reference.
Human reference: icon_set/skills/icon-design/human-reference.md (head on the torso
axis, exact 4-unit detached-head gap).
Lucide construction: no acro-yoga match; stroke limbs and ring head as in
'person-standing'.
Keyshape VRECT_L: centerline x 8 (upper limb tip, head) .. 40 (hook), y 4 (rounded
top) .. 44 (head).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "672c58c9-cf49-5d74-ba11-e6398667c047"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260926T061914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg"
AUTHOR = "claude-opus-5-5"


class AcroYogaFoldedBalance(Solo48):
    icon_id = "acro-yoga-folded-balance"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/yoga"
    aliases = ("acro-yoga-pose",)
    keywords = ("acro-yoga", "yoga", "balance", "partner", "pose", "fitness", "acrobatics")

    def build(self) -> None:
        spine, foot, gap = 24, 22, 8
        # Upper section: lower limb -> spine -> rounded top -> upper limb.
        self.add_line("flyer-lower-limb", (12, foot), (spine, foot))
        self.add_line("flyer-spine-low", (spine, foot), (spine, 10))
        self.add_line("flyer-spine-high", (spine, 10), (spine, 9))
        self.add_arc("flyer-top", (spine, 9), (14, 9), radius_x=5, sweep=False)
        self.add_line("flyer-upper-limb", (14, 9), (8, 14))
        self.add_contour("flyer", "flyer-lower-limb", "flyer-spine-low", "flyer-spine-high",
                         "flyer-top", "flyer-upper-limb")
        self.add_arc("flyer-side", (spine, 10), (spine, foot), radius_x=6, sweep=True)
        self.relate("connect", "flyer", "flyer-side")
        # Lower section: raised arm, lying torso, rounded upward hook.
        top, ground = foot + gap, 40
        self.add_line("base-arm", (spine, top), (spine, ground))
        self.add_line("base-torso", (spine, ground), (36, ground))
        self.add_arc("base-hook", (36, ground), (40, 36), radius_x=4, sweep=False)
        self.add_line("base-shins", (40, 36), (40, 30))
        self.add_contour("base", "base-arm", "base-torso", "base-hook", "base-shins")
        # Base head on the torso axis, 4 + 8 beyond the neck junction (24, 40).
        self.add_arc("base-head-top", (8, ground), (16, ground), radius_x=4, sweep=True)
        self.add_arc("base-head-bottom", (16, ground), (8, ground), radius_x=4, sweep=True)
        self.add_contour("base-head", "base-head-top", "base-head-bottom", closed=True)
        self.mark_human_figure("base", head="base-head", torso="base-torso", torso_junction="start")
