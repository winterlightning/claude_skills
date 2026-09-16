"""Pipe Valve with Round Pivot.
Plan: Vertical pipe stubs, valve housing and a rounded horizontal handle joined by an actual spindle. Housing centered (14,24); handle ends at x44. Bounds (4,8)-(44,40).
References: Lucide glasses for round housing/bridge construction; no direct local valve match.
Reduction: Paired pipe walls and pivot ring reduced to pipe strokes and a round-ended spindle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '576f585b-fdbd-4a2a-9664-420d2118c89a'
SOURCE_PATH = 'pictographic-primitives/construction/valve 1_576f585b-fdbd-4a2a-9664-420d2118c89a.svg'
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


def symmetric(icon, name, start, left_steps, axis=24):
    """One half owns the whole outline; reflect and reverse its traversal."""
    flip = lambda p: (2*axis-p[0], p[1])
    prior = start
    reverse = []
    for kind, end, *args in left_steps:
        if kind == 'B':
            reverse.append((kind, flip(prior), flip(args[1]), flip(args[0])))
        else:
            reverse.append((kind, flip(prior), *args))
        prior = end
    path(icon, name, start, *left_steps, *reversed(reverse), closed=True)


class PipeValveWithRoundPivot(Solo48):
    icon_id = 'pipe-valve-with-round-pivot'
    keyshape = Keyshape.HRECT_L
    category = 'construction'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('pipe', 'valve', 'with', 'round', 'pivot')

    def build(self):
        axis=14
        circle(self,'housing',axis,24,10)

        self.add_line('pipe-top',(axis,8),(axis,14))
        self.add_line('pipe-bottom',(axis,34),(axis,40))
        self.relate('connect','pipe-top','housing')
        self.relate('connect','pipe-bottom','housing')
        self.add_polyline('spindle',(axis,24),(24,24),(33,24))
        self.relate('connect','housing','spindle')

        path(self,'handle',(33,24),('A',(37,20),4,4,True),('L',(40,20)),('A',(44,24),4,4,True),('A',(40,28),4,4,True),('L',(37,28)),('A',(33,24),4,4,True),closed=True)
        self.relate('connect','spindle','handle')
