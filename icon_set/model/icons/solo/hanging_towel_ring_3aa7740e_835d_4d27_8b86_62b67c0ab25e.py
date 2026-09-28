"""Hanging Towel Ring.

Plan: Ring radius14 at (24,28), mount radius4, shared attachment at (24,14). Bounds (6,6)-(42,42). Short connector omitted by joining the physical loops directly.
Construction: Lucide circle: cardinal quarter arcs for the main ring; the original reference owns mounting loop and rail.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3aa7740e-835d-4d27-8b86-62b67c0ab25e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/rounded hanger_3aa7740e-835d-4d27-8b86-62b67c0ab25e.svg'
AUTHOR = "gpt-6"

class Batch03Icon8(Solo48):
    icon_id = 'hanging-towel-ring-3aa7740e'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('hanging-towel-ring',)
    keywords = ('hanging', 'towel', 'ring')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for i, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{i}"
                if kind == "L": self.add_line(member, here, end)
                elif kind == "A": self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == "C": self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, radius):
            path(name,(cx,cy-radius),[("A",(cx+radius,cy),radius,radius,True),("A",(cx,cy+radius),radius,radius,True),("A",(cx-radius,cy),radius,radius,True),("A",(cx,cy-radius),radius,radius,True)],True)
        axis=24
        self.add_polyline("rail",(6,6),(20,6),(28,6),(42,6))
        path("mount",(20,6),[("L",(28,6)),("L",(28,10)),("A",(axis,14),4,4,True),("A",(20,10),4,4,True),("L",(20,6))],True)
        circle("ring",axis,28,14)
        self.relate("connect","mount","rail")
        self.relate("connect","mount","ring")
