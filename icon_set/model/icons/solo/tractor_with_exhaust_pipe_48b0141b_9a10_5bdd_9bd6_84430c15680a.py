"""Tractor with Exhaust Pipe.

Plan: Side-view tractor with wheels sharing y=40 ground, a high cab and a low hood. Wheel radii differ deliberately. Bounds (4,8)-(44,40).
Construction references: Lucide tractor: unequal circular wheels, sparse cab and engine outline.
Simplification: Tire tread and extra cab mullion; fender simplified into body silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48b0141b-9a10-5bdd-9bd6-84430c15680a'
SOURCE_PATH = 'pictographic-primitives/construction/tractor_48b0141b-9a10-5bdd-9bd6-84430c15680a.svg'
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


class TractorWithExhaustPipe(Solo48):
    icon_id = 'tractor-with-exhaust-pipe'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('tractor', 'with', 'exhaust', 'pipe')

    def build(self):
        circle(self,'rear-wheel',13,31,9)
        circle(self,'front-wheel',39,35,5)
        path(self,'body',(13,22),('L',(13,8)),('L',(24,8)),('L',(28,20)),('L',(36,20)),('L',(39,20)),('L',(39,30)))
        self.add_line('chassis',(22,31),(34,35))
        self.relate('connect','chassis','front-wheel')
        self.relate('connect','body','rear-wheel')
        self.relate('connect','body','front-wheel')
        self.relate('connect','chassis','rear-wheel')
        self.add_line('exhaust',(36,10),(36,20))
        self.relate('connect','exhaust','body')
