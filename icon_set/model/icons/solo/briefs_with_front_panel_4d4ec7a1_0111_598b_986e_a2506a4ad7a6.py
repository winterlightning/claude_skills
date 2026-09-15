"""Briefs with Front Panel.

Plan: Briefs with broad waistband, rounded leg openings and mirrored front panel seams. Bounds (4,8)-(44,40).
Construction references: Lucide shirt: simple garment outline and shared seam junctions.
Simplification: Extra stitching and seam offsets.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d4ec7a1-0111-598b-986e-a2506a4ad7a6'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear briefs male_4d4ec7a1-0111-598b-986e-a2506a4ad7a6.svg'
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


class BriefsWithFrontPanel(Solo48):
    icon_id = 'briefs-with-front-panel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('briefs', 'with', 'front', 'panel')

    def build(self):
        path(self,'outline',(6,8),('L',(42,8)),('L',(44,16)),('L',(44,24)),('B',(30,40),(38,24),(32,34)),('L',(18,40)),('B',(4,24),(16,34),(10,24)),('L',(4,16)),('L',(6,8)),closed=True)
        self.add_polyline('waistband',(4,16),(16,16),(32,16),(44,16))
        for side in (-1,1):
            x=lambda v:24+side*v
            self.add_line('panel-'+str(side),(x(8),16),(x(6),40))
            self.relate('connect','outline','panel-'+str(side))
            self.relate('connect','waistband','panel-'+str(side))
        self.relate('connect','outline','waistband')
