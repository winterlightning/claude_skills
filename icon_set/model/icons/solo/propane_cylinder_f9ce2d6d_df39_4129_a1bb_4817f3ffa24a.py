"""Propane Cylinder.

Plan: Centerline extremes (8,4)-(40,44); VRECT_L keyshape supports the complete standalone source silhouette.
Construction: Source-specific squat cylinder with broad cap and flared foot; mirrored shoulders and equal neck supports.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9ce2d6d-df39-4129-a1bb-4817f3ffa24a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/gas_f9ce2d6d-df39-4129-a1bb-4817f3ffa24a.svg'
AUTHOR = "gpt-6"

class Batch04Icon6(Solo48):
    icon_id = 'propane-cylinder-f9ce2d6d'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('propane-cylinder',)
    keywords = ('propane', 'cylinder')

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
        path("tank",(16,14),[("L",(18,14)),("L",(30,14)),("L",(32,14)),("A",(40,22),8,8,True),("L",(40,28)),("A",(32,36),8,8,True),("L",(16,36)),("A",(8,28),8,8,True),("L",(8,22)),("A",(16,14),8,8,True)],True)
        self.add_polyline("cap",(14,4),(18,4),(30,4),(34,4))
        for x in (18,30):
            k=f"neck-{x}";self.add_line(k,(x,4),(x,14));self.relate("connect",k,"cap");self.relate("connect",k,"tank")
        path("foot",(16,36),[("C",(8,44),(12,36),(8,40)),("L",(40,44)),("C",(32,36),(40,40),(36,36))])
        self.relate("connect","foot","tank")
