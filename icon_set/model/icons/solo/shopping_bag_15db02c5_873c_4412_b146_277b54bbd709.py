"""Shopping Bag.

Plan: Centerline extremes (8,4)-(40,44); VRECT_L keyshape supports the complete standalone source silhouette.
Construction: Lucide shopping-bag: bag with tall arch handle. The source supplies tapered sides and handle ends that descend inside the face.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15db02c5-873c-4412-b146-277b54bbd709'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/bag 3_15db02c5-873c-4412-b146-277b54bbd709.svg'
AUTHOR = "gpt-6"

class Batch04Icon13(Solo48):
    icon_id = 'shopping-bag-15db02c5'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
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
        self.add_polyline("body",(10,18),(18,18),(30,18),(38,18),(40,44),(8,44),closed=True)
        path("handle",(18,24),[("L",(18,18)),("L",(18,10)),("A",(30,10),6,6,True),("L",(30,18)),("L",(30,24))])
        self.relate("connect","body","handle")
