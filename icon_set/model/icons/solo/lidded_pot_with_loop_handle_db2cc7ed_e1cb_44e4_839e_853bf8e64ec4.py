"""Lidded Pot with Side Handle.

Plan: Asymmetric vessel with left pouring lip, right half-ellipse handle, centered domed lid. Bounds (6,6)-(42,42).
Construction: Lucide cooking-pot: structural rim and rounded body; supplied source owns domed lid, pouring notch and right loop handle.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db2cc7ed-e1cb-44e4-839e-853bf8e64ec4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/pot 1_db2cc7ed-e1cb-44e4-839e-853bf8e64ec4.svg'
AUTHOR = "gpt-6"

class Batch03Icon10(Solo48):
    icon_id = 'lidded-pot-with-loop-handle-db2cc7ed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('lidded-pot-with-loop-handle',)
    keywords = ('lidded', 'pot', 'with', 'loop', 'handle')

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
        path("body",(6,18),[("L",(10,18)),("L",(30,18)),("L",(32,18)),("L",(32,34)),("L",(32,38)),("A",(28,42),4,4,True),("L",(14,42)),("A",(10,38),4,4,True),("L",(10,26)),("L",(6,18))],True)
        path("lid",(10,18),[("A",(20,10),10,8,True),("A",(30,18),10,8,True)])
        self.add_line("knob",(20,6),(20,10))
        path("handle",(32,18),[("A",(32,34),10,8,True)])
        for a,b in [("body","lid"),("lid","knob"),("body","handle")]:self.relate("connect",a,b)
