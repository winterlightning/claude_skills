"""Halter Bikini Set.

Plan: Two coordinated bikini pieces, mirrored cups and curved leg openings; halter ties share the central top node. Bounds (6,6)-(42,42).
Construction references: Lucide shirt: garment silhouette with minimal internal strokes.
Simplification: Double waistband reduced to the top edge; tiny central clasp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4cfb47e-5b0a-4abd-9ef1-99a92f12bf21'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear bikini_d4cfb47e-5b0a-4abd-9ef1-99a92f12bf21.svg'
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


class HalterBikiniSet(Solo48):
    icon_id = 'halter-bikini-set'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('halter', 'bikini', 'set')

    def build(self):
        path(self,'top',(24,14),('B',(6,14),(18,10),(6,10)),('B',(24,18),(6,26),(18,26)),('B',(42,14),(30,26),(42,26)),('B',(24,14),(42,10),(30,10)),closed=True)
        self.add_polyline('ties',(16,6),(24,14),(32,6))
        path(self,'bottom',(6,32),('L',(42,32)),('B',(30,42),(34,32),(34,38)),('L',(18,42)),('B',(6,32),(14,38),(14,32)),closed=True)
        self.relate('connect','ties','top')
