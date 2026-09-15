"""Lace-Trim Bra.

Plan: Two mirrored rounded bra cups with tall straps and a simplified scalloped neckline. Bounds (4,8)-(44,40).
Construction references: Lucide shirt for garment reduction; source for cups and scalloped neckline.
Simplification: Fine lace reduced to one broad scallop per cup; secondary cup seam removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39d8b35a-f172-55f8-9cd5-8220f30ca383'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear bra lace_39d8b35a-f172-55f8-9cd5-8220f30ca383.svg'
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


class LaceTrimBra(Solo48):
    icon_id = 'lace-trim-bra'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('lace-trim', 'bra')

    def build(self):
        path(self,'cups',(4,20),('A',(14,20),5,5,True),('B',(24,30),(19,20),(24,25)),('B',(34,20),(24,25),(29,20)),('A',(44,20),5,5,True),('L',(44,30)),('A',(34,40),10,10,True),('A',(24,30),10,10,True),('A',(14,40),10,10,True),('A',(4,30),10,10,True),('L',(4,20)),closed=True)
        for side in (-1,1):
            x=24+side*20
            self.add_line('strap-'+str(side),(x,8),(x,20))
            self.relate('connect','cups','strap-'+str(side))
