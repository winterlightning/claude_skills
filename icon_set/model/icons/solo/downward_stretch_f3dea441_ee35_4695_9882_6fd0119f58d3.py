"""A person in the yoga downward stretch: hips raised high, body folded into an inverted V,
head low beside the hands.

Symbol plan: one stick figure. The body is one polyline: the feet at (44, 40), the legs
up to the raised hips (32, 8), the back down to the shoulders' low point (24, 36) and a
short level upper-torso run to the neck (20, 36), as in the reference's flat bottom-left
stroke. The r4 head sits straight beside the neck at (8, 36): its outline is exactly 8
from the neck end on the horizontal axis (4 units of visible ink), following the level
upper torso. The level run is what lets the head gap be certified. An r3 head with a slightly
wider V (attempts/v2-r3-head.svg) read as a dot and barely widened the V, so the r4 head
stays.
Human reference: icon_set/references/human_ref/full_body_ref.png (round head, single
round-ended body strokes, detached head with a 4-unit ink gap).
Lucide construction: no Lucide yoga pose; straight strokes with round joins as in
Lucide's person pictograms.
Keyshape HRECT_L: centerline x 4..44 (head, feet), y 8..40 (hips, head bottom and feet).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "f3dea441-ee35-4695-9882-6fd0119f58d3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__downward-stretch/20260926T055140Z-thuan-mac/reference/yoga down stretch_f3dea441-ee35-4695-9882-6fd0119f58d3.svg"
AUTHOR = "claude-opus-5-5"


class DownwardStretch(Solo48):
    icon_id = "downward-stretch-solo"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/sport"
    aliases = ("yoga down stretch", "downward dog", "adho mukha svanasana")
    keywords = ("yoga", "stretch", "downward dog", "pose", "exercise", "fitness", "pilates", "workout")

    def build(self) -> None:
        feet, hips, shoulders, neck = (44, 40), (32, 8), (24, 36), (20, 36)
        self.add_line("legs", feet, hips)
        self.add_line("back", hips, shoulders)
        self.add_line("upper-torso", shoulders, neck)
        self.add_contour("body", "legs", "back", "upper-torso")
        r = 4
        cx, cy = neck[0] - 8 - r, neck[1]
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ("head-w", "head-n", "head-e", "head-s")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("head", *names, closed=True)
        self.mark_human_figure("yogi", head="head", torso="upper-torso", torso_junction="end")
