"""Hexagonal Molecular Ring.

Plan: Three equal radius3 nodes at the alternating vertices, explicit cardinal bond attachments. Bounds (6,6)-(42,42).
Construction: Lucide circle: equal cardinal arcs for node outlines; original source owns the alternating node hexagon.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b063dc0-3f96-438d-b587-2f87393eb9fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/molecule cube_0b063dc0-3f96-438d-b587-2f87393eb9fe.svg'
AUTHOR = "gpt-6"

class Batch03Icon9(Solo48):
    icon_id = 'hexagonal-molecular-ring-0b063dc0'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('hexagonal-molecular-ring',)
    keywords = ('hexagonal', 'molecular', 'ring')

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
        axis=24;radius=3
        for name,x,y in [("top",axis,9),("left",9,33),("right",39,33)]:circle(name,x,y,radius)
        for side,node in [(-1,"left"),(1,"right")]:
            p=lambda x,y:(axis+side*x,y)
            name=f"upper-bond-{side}"
            self.add_polyline(name,p(3,9),p(15,18),p(15,30))
            self.relate("connect",name,"top");self.relate("connect",name,node)
        self.add_polyline("lower-bonds",(9,36),(axis,42),(39,36))
        for node in ("left","right"):self.relate("connect","lower-bonds",node)
