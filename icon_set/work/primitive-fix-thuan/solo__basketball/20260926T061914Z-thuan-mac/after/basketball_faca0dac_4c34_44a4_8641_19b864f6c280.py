"""Basketball: a ball with its seams - a vertical and a horizontal seam through the
centre and two side seams curving in toward the middle.

Symbol plan: the ball is a radius-20 circle about the canvas centre (the largest
CIRCLE allows), split into eight arcs at the seam junctions (24,4), (44,24),
(24,44), (4,24) and the side-seam ends (8,12), (8,36), (40,12), (40,36), all
integer points of that circle. The central seams are straight lines. Each side
seam is two tangent cubics bowing inward from the circle to an apex 9 from the
vertical seam, where it crosses the horizontal seam with a vertical tangent;
the right seam mirrors the left about x=24.
Revision (reviewer: "deepen both inward curves and enlarge the circle slightly
within the frame. Keep the central vertical and horizontal lines straight"): the
side seams, which bowed slightly outward, now bow 7 units inward; the circle is
already at the keyshape's full radius 20, so it cannot grow further.
Lucide construction: 'volleyball'/'dribbble' - circle with curved seams.
Keyshape CIRCLE: radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "faca0dac-4c34-44a4-8641-19b864f6c280"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__basketball/20260926T061914Z-thuan-mac/reference/basketball_faca0dac-4c34-44a4-8641-19b864f6c280.svg"
AUTHOR = "claude-opus-5-5"


def mx(p):
    return (48 - p[0], p[1])


class Basketball(Solo48):
    icon_id = "basketball"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("ball",)
    keywords = ("basketball", "ball", "sport", "game", "court", "hoop")

    def build(self) -> None:
        nodes = [(24, 4), (40, 12), (44, 24), (40, 36), (24, 44), (8, 36), (4, 24), (8, 12)]
        ring = []
        for i, a in enumerate(nodes):
            self.add_arc(f"ball-{i}", a, nodes[(i + 1) % 8], radius_x=20, sweep=True)
            ring.append(f"ball-{i}")
        self.add_contour("ball", *ring, closed=True)
        apex = 15
        self.add_polyline("seam-vertical", (24, 4), (24, 24), (24, 44))
        self.add_polyline("seam-horizontal", (4, 24), (apex, 24), (24, 24), mx((apex, 24)), (44, 24))
        for name, f in (("left", lambda p: p), ("right", mx)):
            self.add_bezier(f"seam-{name}", f((8, 12)),
                            (f((11, 16)), f((apex, 20)), f((apex, 24))),
                            (f((apex, 28)), f((11, 32)), f((8, 36))))
            self.relate("connect", f"seam-{name}", "ball")
            self.relate("connect", f"seam-{name}", "seam-horizontal")
        self.relate("connect", "seam-vertical", "seam-horizontal")
        self.relate("connect", "seam-vertical", "ball")
        self.relate("connect", "seam-horizontal", "ball")
