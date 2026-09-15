"""Tennis Court Plan.

Plan: A tennis court owns three horizontal lanes, mirrored service boxes and the central net. Shared grid nodes create every actual junction. Bounds (4,8)-(44,40).
Construction references: Lucide network for shared orthogonal junctions.
Simplification: No court features omitted; proportions opened for 4-unit ink clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '026dac7a-d97d-5401-a3c4-46d1b41678b2'
SOURCE_PATH = 'pictographic-primitives/building/tennis court_026dac7a-d97d-5401-a3c4-46d1b41678b2.svg'
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


class TennisCourtPlan(Solo48):
    icon_id = 'tennis-court-plan'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('tennis', 'court', 'plan')

    def build(self):
        xs = (4,14,24,34,44)
        ys = (8,16,24,32,40)
        # Every line is split at its genuine court junctions.
        for row,y in enumerate(ys):
            active = xs[1:4] if y == 24 else xs
            self.add_polyline(f'horizontal-{row}', *((x,y) for x in active))
        for col,x in enumerate(xs):
            active = ys[1:4] if x in (14,34) else ys
            self.add_polyline(f'vertical-{col}', *((x,y) for y in active))
        for row,y in enumerate(ys):
            for col,x in enumerate(xs):
                if (y != 24 or x in (14,24,34)) and (x not in (14,34) or y in (16,24,32)):
                    self.relate('connect',f'horizontal-{row}',f'vertical-{col}')
