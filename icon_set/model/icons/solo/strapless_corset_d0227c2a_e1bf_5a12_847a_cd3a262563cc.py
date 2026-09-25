"""Strapless Corset.

Plan: Mirrored fitted corset, sweetheart neck and a pointed lower center; waist and neckline use coherent tangent curves. Bounds (8,4)-(40,44).
Construction references: Lucide shirt for coherent garment contour; source for fitted silhouette.
Simplification: Broken front seam reduced to a single short center stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0227c2a-e1bf-5a12-847a-cd3a262563cc'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear corset_d0227c2a-e1bf-5a12-847a-cd3a262563cc.svg'
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


class StraplessCorset(Solo48):
    icon_id = 'strapless-corset'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('strapless', 'corset')

    def build(self):
        axis=24
        path(self,'outline',(8,4),('B',(24,12),(16,4),(20,8)),('B',(40,4),(28,8),(32,4)),('B',(36,24),(40,12),(36,17)),('B',(40,36),(36,28),(38,32)),('B',(24,44),(34,38),(28,40)),('B',(8,36),(20,40),(14,38)),('B',(12,24),(10,32),(12,28)),('B',(8,4),(12,17),(8,12)),closed=True)
        self.add_line('front-seam',(axis,22),(axis,30))
