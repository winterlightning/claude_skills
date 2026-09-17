"""Raised Open Hand.

Plan: Centerline extremes (4,8)-(44,40); HRECT_L keyshape supports the complete standalone source silhouette.
Construction: Lucide hand and the original reference inform the unequal fingers and asymmetric thumb. Shared human guidance consulted; head-body spacing does not apply to a hand.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6150ab7-8e7e-4d9a-a048-0ead02521414'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/hand 1_a6150ab7-8e7e-4d9a-a048-0ead02521414.svg'
AUTHOR = "gpt-6"

class Batch04Icon10(Solo48):
    icon_id = 'raised-open-hand-a6150ab7'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hand"
    aliases = ('raised-open-hand',)
    keywords = ('raised', 'open', 'hand')

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
        path("outline",(12,28),[("L",(12,16)),("A",(20,16),4,4,True),("L",(20,12)),("A",(28,12),4,4,True),("L",(28,16)),("A",(36,16),4,4,True),("L",(36,22)),("A",(44,22),4,4,True),("L",(44,28)),("A",(32,40),12,12,True),("L",(24,40)),("C",(4,26),(14,40),(10,34)),("C",(12,28),(4,20),(10,22))],True)
        for x,y,end in [(20,16,24),(28,16,24),(36,22,26)]:
            k=f"finger-{x}";self.add_line(k,(x,y),(x,end));self.relate("connect","outline",k)
