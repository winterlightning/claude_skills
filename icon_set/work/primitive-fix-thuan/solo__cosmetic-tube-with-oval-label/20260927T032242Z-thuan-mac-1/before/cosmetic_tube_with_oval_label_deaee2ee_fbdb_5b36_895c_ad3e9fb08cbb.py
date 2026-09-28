"""Cosmetic Tube with Oval Label.

Plan: Upright cosmetic tube with narrow top cap, widening body, oval label and bottom band. Bounds (8,4)-(40,44).
Construction references: Lucide watch: narrow attachment atop a rounded body; oval label reauthored separately.
Simplification: Small shoulder facets and cap side seams; oval label turned horizontal to open its surrounding space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deaee2ee-fbdb-5b36-895c-ad3e9fb08cbb'
SOURCE_PATH = 'pictographic-primitives/beauty/tube_deaee2ee-fbdb-5b36-895c-ad3e9fb08cbb.svg'
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


class CosmeticTubeWithOvalLabel(Solo48):
    icon_id = 'cosmetic-tube-with-oval-label'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('cosmetic', 'tube', 'with', 'oval', 'label')

    def build(self):
        self.add_polyline('cap',(16,12),(16,4),(32,4),(32,12))
        path(self,'body',(16,12),('L',(32,12)),('L',(36,12)),('L',(40,36)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,36)),('L',(12,12)),('L',(16,12)),closed=True)
        self.add_line('band',(8,36),(40,36))
        path(self,'label',(20,24),('A',(28,24),4,3,True),('A',(20,24),4,3,True),closed=True)
        self.relate('connect','cap','body')
        self.relate('connect','band','body')
