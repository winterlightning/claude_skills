"""Three-Stage Funnel.
Plan: Three separated decreasing funnel stages centered on x24. Bounds (8,4)-(40,44); 8-unit clear centerline bands.
References: Lucide funnel for sloping intake; supplied source for three disconnected stages.
Reduction: No stage omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '317401b3-a6a1-407a-a40e-3db88f11c5b7'
SOURCE_PATH = 'pictographic-primitives/business/workflow coaching pipeline management_317401b3-a6a1-407a-a40e-3db88f11c5b7.svg'
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

class ThreeStageFunnel(Solo48):
    icon_id = 'three-stage-funnel'
    keyshape = Keyshape.VRECT_L
    category = 'business'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('three-stage', 'funnel')
    def build(self):
        self.add_polyline('stage-1',(8,4),(40,4),(34,12),(14,12),closed=True)
        self.add_polyline('stage-2',(14,20),(34,20),(28,28),(20,28),closed=True)
        self.add_polyline('stage-3',(20,36),(28,36),(28,44),(20,44),closed=True)
