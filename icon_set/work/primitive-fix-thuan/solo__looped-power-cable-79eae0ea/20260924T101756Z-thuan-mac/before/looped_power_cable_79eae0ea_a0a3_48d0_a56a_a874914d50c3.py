"""Looped Power Cable.

Plan: Large lower semicircle radius18 with tangent left shoulder to the plug. Paired prongs separated8. Bounds (6,6)-(42,42).
Construction: Lucide plug and circle: rounded plug body, paired prongs and broad cable loop; preserve the open cable end.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79eae0ea-a0a3-48d0-a56a-a874914d50c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/circle cable_79eae0ea-a0a3-48d0-a56a-a874914d50c3.svg'
AUTHOR = "gpt-6"

class Batch03Icon13(Solo48):
    icon_id = 'looped-power-cable-79eae0ea'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/cable"
    aliases = ('looped-power-cable',)
    keywords = ('looped', 'power', 'cable')

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
        path("cable",(20,10),[("C",(6,24),(12,10),(6,16)),("A",(42,24),18,18,False)])
        path("plug",(20,10),[("A",(24,6),4,4,True),("L",(32,6)),("L",(32,14)),("L",(24,14)),("A",(20,10),4,4,True)],True)
        self.relate("connect","cable","plug")
        for y in (6,14):
            n=f"prong-{y}";self.add_line(n,(32,y),(40,y));self.relate("connect","plug",n)
