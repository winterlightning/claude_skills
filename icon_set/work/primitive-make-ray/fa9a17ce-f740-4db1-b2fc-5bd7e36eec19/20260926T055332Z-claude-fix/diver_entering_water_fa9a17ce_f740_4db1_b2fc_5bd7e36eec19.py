"""A diver plunging diagonally into the water: legs up behind, arms reaching into the waves.

Symbol plan: a stick figure over a wave line. Waves: three half-ellipse troughs (rx 6,
ry 4) between cusps at x 6, 18, 30, 42 on y 38, bottoming at y 42. Body: one polyline
from the feet (8, 6) down to the hip (13, 16), the torso to the shoulder (20, 21) and a
short horizontal neck to (23, 21). The arms leave the shoulder and reach down-right into
the water at the cusp (30, 38) (shared endpoint, declared). The r5 head sits beside the
neck at (36, 21): its outline is exactly 8 from the neck end on the horizontal axis
(4 units of visible ink), following the neck direction; the arms pass 8.8+ from it. A longer neck with an r4 head (attempts/v1-*) read as a cross.
Human reference: icon_set/references/human_ref/full_body_ref.png (round head, round-ended
limb strokes, detached head with a 4-unit ink gap).
Lucide construction: 'waves' (repeated troughs) for the water; no Lucide diver exists.
Keyshape SQUARE: centerline x 6..42 (waves, head right), y 6..42 (feet, wave troughs).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fa9a17ce-f740-4db1-b2fc-5bd7e36eec19"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diver-entering-water/20260926T055140Z-thuan-mac/reference/swimming diving_fa9a17ce-f740-4db1-b2fc-5bd7e36eec19.svg"
AUTHOR = "claude-opus-5-5"


class DiverEnteringWater(Solo48):
    icon_id = "diver-entering-water"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/sport"
    aliases = ("swimming diving", "diving", "diver")
    keywords = ("dive", "diving", "swimming", "swimmer", "pool", "water", "sport", "plunge", "jump")

    def build(self) -> None:
        # water
        crest, trough, half = 38, 42, 6
        xs = (6, 18, 30, 42)
        waves = []
        for i in range(3):
            n = f"wave-{i + 1}"
            self.add_arc(n, (xs[i], crest), (xs[i + 1], crest), radius_x=half, radius_y=trough - crest,
                         sweep=False)
            waves.append(n)
        self.add_contour("water", *waves)
        # body
        feet, hip, shoulder, neck = (8, 6), (13, 16), (20, 21), (23, 21)
        self.add_line("legs", feet, hip)
        self.add_line("torso", hip, shoulder)
        self.add_line("neck", shoulder, neck)
        self.add_contour("body", "legs", "torso", "neck")
        self.add_line("arms", shoulder, (30, crest))
        self.relate("connect", "body", "arms")
        self.relate("connect", "arms", "water")
        # head beside the neck: 8 from the neck end on the horizontal axis
        r = 5
        cx, cy = neck[0] + 8 + r, neck[1]
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        hn = ("head-w", "head-n", "head-e", "head-s")
        for i, n in enumerate(hn):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("head", *hn, closed=True)
        self.mark_human_figure("diver", head="head", torso="neck", torso_junction="end")
