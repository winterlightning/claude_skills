"""Fringed Rug.

Plan: Rectangle with five fringes on each short edge, step8, common length6. Bounds (8,4)-(40,44). Reduce source fringe count to keep 4u ink gaps.
Construction: No useful local Lucide rug match. Use a simple joined rectangle and evenly repeated straight fringe.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c637baf-14e5-43aa-9d09-6ed1e42e5a7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/mat_0c637baf-14e5-43aa-9d09-6ed1e42e5a7b.svg'
AUTHOR = "gpt-6"

class Batch03Icon1(Solo48):
    icon_id = 'fringed-area-rug-0c637baf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/rug"
    aliases = ('fringed-area-rug',)
    keywords = ('fringed', 'area', 'rug')

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
        left,right,top,bottom,step=8,40,10,38,8
        xs=list(range(left,right+1,step))
        self.add_polyline("rug",*[(x,top) for x in xs],*[(x,bottom) for x in reversed(xs)],closed=True)
        for i,x in enumerate(xs):
            for name,y,end in [("top",top,4),("bottom",bottom,44)]:
                k=f"fringe-{name}-{i}"
                self.add_line(k,(x,y),(x,end))
                self.relate("connect","rug",k)
