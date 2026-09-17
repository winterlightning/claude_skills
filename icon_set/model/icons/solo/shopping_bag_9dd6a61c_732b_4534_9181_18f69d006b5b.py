"""Shopping Bag.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide shopping-bag informs the joined handle and body. Source owns the tall arch and tapered sides.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9dd6a61c-732b-4534-9181-18f69d006b5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/bag 1_9dd6a61c-732b-4534-9181-18f69d006b5b.svg'
AUTHOR = "gpt-6"
class Batch05Icon0(Solo48):
    icon_id = 'shopping-bag-9dd6a61c'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/bag"
    aliases = ('shopping-bag',)
    keywords = ('shopping', 'bag')
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
        axis=24;left=axis-16;right=axis+16
        self.add_polyline("body",(left+2,18),(axis-6,18),(axis+6,18),(right-2,18),(right,44),(left,44),closed=True)
        path("handle",(axis-6,24),[("L",(axis-6,18)),("L",(axis-6,10)),("A",(axis+6,10),6,6,True),("L",(axis+6,18)),("L",(axis+6,24))]);self.relate("connect","body","handle")
