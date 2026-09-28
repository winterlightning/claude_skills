"""Ball with lines: a soccer-style ball - a small central pentagon with five seams
running out to the ball's outline.

Symbol plan: the ball is a radius-20 circle about the canvas centre, split into
arcs at the five seam ends (24,4), (44,24), (36,40), (12,40), (4,24) - integer
points of that circle. The pentagon (point up, mirrored about x=24) puts each
vertex on the ray from the centre to its seam end, so every seam is radial:
top (24,16), sides (16,24)/(32,24), base (19,30)/(29,30). It spans 16 x 14, a
third of the ball.
Revision (reviewer: "Make the inner pentagon smaller"): the rejected drawing had a
large hexagon with six seams; this is the reference's pentagon, smaller.
Lucide construction: no soccer ball; radial spokes to a circle as in 'ship-wheel'.
Keyshape CIRCLE: radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "02c70f52-9dee-4f13-8c03-a5f8a38f8a84"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__ball-with-lines/20260926T061914Z-thuan-mac/reference/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.svg"
AUTHOR = "claude-opus-5-5"


class BallWithLines(Solo48):
    icon_id = "ball-with-lines"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("soccer-ball", "football")
    keywords = ("ball", "soccer", "football", "sport", "pentagon", "game")

    def build(self) -> None:
        ends = [(24, 4), (44, 24), (36, 40), (12, 40), (4, 24)]
        pentagon = [(24, 16), (32, 24), (29, 30), (19, 30), (16, 24)]
        ring = []
        for i, a in enumerate(ends):
            self.add_arc(f"ball-{i}", a, ends[(i + 1) % 5], radius_x=20, sweep=True)
            ring.append(f"ball-{i}")
        self.add_contour("ball", *ring, closed=True)
        self.add_polyline("pentagon", *pentagon, closed=True)
        for i, (v, e) in enumerate(zip(pentagon, ends)):
            self.add_line(f"seam-{i}", v, e)
            self.relate("connect", f"seam-{i}", "pentagon")
            self.relate("connect", f"seam-{i}", "ball")
