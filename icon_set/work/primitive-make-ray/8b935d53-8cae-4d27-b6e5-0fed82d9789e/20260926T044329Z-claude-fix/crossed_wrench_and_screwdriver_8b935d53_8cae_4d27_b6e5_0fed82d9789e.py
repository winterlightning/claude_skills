"""A crossed wrench and screwdriver: a double open-end wrench from top left to bottom right over a screwdriver from bottom left to top right.

Symbol plan: the wrench lies on the diagonal x=y: a straight shaft between two U jaws,
each a half circle of radius 4*sqrt2 (two cubic quarters through integer tip/back
knots) with short prongs opening outward; the bottom-right jaw is the top-left one
rotated 180 degrees about (24,24). The screwdriver lies on x+y=48: a handle outlined as
a tube (sides x+y=42 and x+y=54, 8.5 apart) with flat ends, and a shaft from the middle
of the handle's top end to the tip. The two shafts cross at the exact node (24,24),
where both are split and joined.
Lucide construction: 'wrench' and 'screwdriver' in a crossed-tools layout.
Keyshape SQUARE: centerline x 6..42, y 6..42 (jaw prongs, handle corners).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8b935d53-8cae-4d27-b6e5-0fed82d9789e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crossed-wrench-and-screwdriver/20260926T044250Z-thuan-mac/reference/tools wrench screwdriver_8b935d53-8cae-4d27-b6e5-0fed82d9789e.svg"
AUTHOR = "claude-opus-5-5"


def _rot(p):
    """Rotate 180 degrees about (24,24)."""
    return (48 - p[0], 48 - p[1])


class CrossedWrenchAndScrewdriver(Solo48):
    icon_id = "crossed-wrench-and-screwdriver"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("tools wrench screwdriver", "tools", "repair tools")
    keywords = ("wrench", "screwdriver", "tools", "repair", "settings", "maintenance", "fix", "service")

    def build(self) -> None:
        cross = (24, 24)
        k = 0.5523 * 4
        j = (12, 12)
        back, tip_a, tip_b = (16, 16), (16, 8), (8, 16)
        prong_a, prong_b = (14, 6), (6, 14)
        for side, f in (("tl", lambda p: p), ("br", _rot)):
            def g(x, y):
                return f((x, y))
            self.add_line(f"prong-{side}-a", f(prong_a), f(tip_a))
            self.add_bezier(f"jaw-{side}-a", f(tip_a), (g(tip_a[0] + k, tip_a[1] + k), g(back[0] + k, back[1] - k), f(back)))
            self.add_bezier(f"jaw-{side}-b", f(back), (g(back[0] - k, back[1] + k), g(tip_b[0] + k, tip_b[1] + k), f(tip_b)))
            self.add_line(f"prong-{side}-b", f(tip_b), f(prong_b))
            self.add_contour(f"jaw-{side}", f"prong-{side}-a", f"jaw-{side}-a", f"jaw-{side}-b", f"prong-{side}-b")
        self.add_line("wrench-shaft-a", back, cross)
        self.add_line("wrench-shaft-b", cross, _rot(back))
        self.add_contour("wrench-shaft", "wrench-shaft-a", "wrench-shaft-b")
        self.relate("connect", "jaw-tl", "wrench-shaft")
        self.relate("connect", "jaw-br", "wrench-shaft")
        # screwdriver handle: sides x+y=42 / 54, ends x-y=-30 (bottom) / -14 (top)
        c1, c2, c3, c4 = (6, 36), (12, 42), (20, 34), (14, 28)
        top_mid = (17, 31)
        self.add_polyline("handle", top_mid, c4, c1, c2, c3, top_mid)
        self.add_line("driver-shaft-a", top_mid, cross)
        self.add_line("driver-shaft-b", cross, (37, 11))
        self.add_contour("driver-shaft", "driver-shaft-a", "driver-shaft-b")
        self.relate("connect", "handle", "driver-shaft")
        self.relate("connect", "wrench-shaft", "driver-shaft")
