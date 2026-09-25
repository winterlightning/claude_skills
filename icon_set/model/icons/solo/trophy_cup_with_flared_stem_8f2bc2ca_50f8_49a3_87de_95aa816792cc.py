"""Trophy Cup with Flared Stem.

Plan: Mirrored handles share cup attachment nodes; rounded bowl and centered stem sit over a low pedestal. Bounds (6,6)-(42,42).
Construction references: Lucide trophy: cup semicircle, symmetric handles and pedestal.
Simplification: Fine rim omitted; flared stem retained as a wide triangular support.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f2bc2ca-50f8-49a3-87de-95aa816792cc'
SOURCE_PATH = 'pictographic-primitives/business/trophy_8f2bc2ca-50f8-49a3-87de-95aa816792cc.svg'
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


class TrophyCupWithFlaredStem(Solo48):
    icon_id = 'trophy-cup-with-flared-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('trophy', 'cup', 'with', 'flared', 'stem')

    def build(self):
        path(self,'bowl',(16,6),('L',(32,6)),('L',(32,14)),('L',(32,22)),('A',(24,30),8,8,True),('A',(16,22),8,8,True),('L',(16,14)),('L',(16,6)),closed=True)
        for side in (-1,1):
            x=lambda offset:24+side*offset
            name='left' if side<0 else 'right'
            path(self,'handle-'+name,(x(8),6),('A',(x(18),14),10,8,side>0),('A',(x(8),22),10,8,side>0))
            self.relate('connect','bowl','handle-'+name)
        self.add_polyline('stem',(24,30),(32,42),(16,42),(24,30))
        self.add_polyline('base',(10,42),(16,42),(32,42),(38,42))
        self.relate('connect','stem','base')
        self.relate('connect','stem','bowl')
