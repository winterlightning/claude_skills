"""Handleless Trophy Cup.

Plan: Handleless round-bottom cup, projecting rim, centered single stem and low pedestal. Bounds (8,4)-(40,44).
Construction references: Lucide trophy: circular bowl bottom and centered pedestal.
Simplification: Double rim and double stem edges reduced to single clean strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38e67035-529b-4b0a-840e-94882a8f48d7'
SOURCE_PATH = 'pictographic-primitives/business/trophy_38e67035-529b-4b0a-840e-94882a8f48d7.svg'
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


class HandlelessTrophyCup(Solo48):
    icon_id = 'handleless-trophy-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('handleless', 'trophy', 'cup')

    def build(self):
        path(self,'bowl',(12,4),('L',(36,4)),('L',(36,16)),('A',(24,28),12,12,True),('A',(12,16),12,12,True),('L',(12,4)),closed=True)
        self.add_polyline('rim',(8,4),(12,4),(36,4),(40,4))
        self.add_line('stem',(24,28),(24,36))
        self.add_polyline('base',(12,44),(12,36),(24,36),(36,36),(36,44),closed=True)
        self.relate('connect','rim','bowl')
        self.relate('connect','stem','bowl')
        self.relate('connect','stem','base')
