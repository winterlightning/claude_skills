"""Jeans with Front Pockets.

Plan: Mirrored long jeans outline with broad legs, V crotch, paired quarter-circle pocket mouths and short fly. Bounds (8,4)-(40,44).
Construction references: Lucide shirt: joined garment outline and sparse seams.
Simplification: Pocket topstitching and belt loops.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e2712a5-c98b-5804-829c-d642a1658577'
SOURCE_PATH = 'pictographic-primitives/clothes/trousers jeans_1e2712a5-c98b-5804-829c-d642a1658577.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


class JeansWithFrontPockets(Solo48):
    icon_id = 'jeans-with-front-pockets'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('jeans', 'with', 'front', 'pockets')

    def build(self):
        self.add_polyline('outline',(8,4),(16,4),(24,4),(32,4),(40,4),(40,12),(40,44),(28,44),(24,26),(20,44),(8,44),(8,12),closed=True)
        self.add_arc('left-pocket',(16,4),(8,12),radius_x=8)
        self.add_arc('right-pocket',(40,12),(32,4),radius_x=8)
        self.add_line('fly',(24,4),(24,12))
        for name in ('left-pocket','right-pocket','fly'):
            self.relate('connect','outline',name)
