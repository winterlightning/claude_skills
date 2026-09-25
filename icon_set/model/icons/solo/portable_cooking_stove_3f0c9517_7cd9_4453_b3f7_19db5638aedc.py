"""Portable Cooking Stove.

Plan: Centerline extremes (6,6)-(42,42); SQUARE keyshape supports the complete standalone source silhouette.
Construction: Lucide cooking-pot: joined rounded appliance structure. Source owns the sloping blank top, front band and projecting foot. Control marks meet the band to preserve spacing.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f0c9517-7cd9-4453-b3f7-19db5638aedc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/stove 1_3f0c9517-7cd9-4453-b3f7-19db5638aedc.svg'
AUTHOR = "gpt-6"

class Batch04Icon4(Solo48):
    icon_id = 'portable-cooking-stove-3f0c9517'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('portable-cooking-stove',)
    keywords = ('portable', 'cooking', 'stove')

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
        path("upper",(6,20),[("L",(10,10)),("C",(16,6),(11,7),(13,6)),("L",(32,6)),("C",(38,10),(35,6),(37,7)),("L",(42,20))])
        path("band",(6,20),[("L",(16,20)),("L",(32,20)),("L",(42,20)),("L",(42,30)),("A",(38,34),4,4,True),("L",(10,34)),("A",(6,30),4,4,True),("L",(6,20))],True)
        path("foot",(10,34),[("C",(16,42),(10,38),(12,42)),("L",(32,42)),("C",(38,34),(36,42),(38,38))])
        self.relate("connect","upper","band");self.relate("connect","foot","band")
        for x in (16,32):
            k=f"control-{x}";self.add_line(k,(x,20),(x,26));self.relate("connect","band",k)
