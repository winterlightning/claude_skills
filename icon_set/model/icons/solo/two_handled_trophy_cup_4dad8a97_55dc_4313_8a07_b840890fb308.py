"""Two-Handled Trophy Cup.

Plan: Mirrored handles share cup attachment nodes; rounded bowl and centered stem sit over a low pedestal. Bounds (6,6)-(42,42).
Construction references: Lucide trophy: cup semicircle, symmetric handles and pedestal.
Simplification: Fine rim and pedestal depth omitted; base retained as a clean baseline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dad8a97-55dc-4313-8a07-b840890fb308'
SOURCE_PATH = 'pictographic-primitives/business/trophy_4dad8a97-55dc-4313-8a07-b840890fb308.svg'
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


class TwoHandledTrophyCup(Solo48):
    icon_id = 'two-handled-trophy-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('business', 'state')
    aliases = ()
    keywords = ('two-handled', 'trophy', 'cup')

    def build(self):
        path(self,'bowl',(16,6),('L',(32,6)),('L',(32,14)),('L',(32,22)),('A',(24,30),8,8,True),('A',(16,22),8,8,True),('L',(16,14)),('L',(16,6)),closed=True)
        for side in (-1,1):
            x=lambda offset:24+side*offset
            name='left' if side<0 else 'right'
            path(self,'handle-'+name,(x(8),6),('A',(x(18),14),10,8,side>0),('A',(x(8),22),10,8,side>0))
            self.relate('connect','bowl','handle-'+name)
        self.add_line('stem',(24,30),(24,42))
        self.add_polyline('base',(14,42),(24,42),(34,42))
        self.relate('connect','stem','base')
        self.relate('connect','stem','bowl')
