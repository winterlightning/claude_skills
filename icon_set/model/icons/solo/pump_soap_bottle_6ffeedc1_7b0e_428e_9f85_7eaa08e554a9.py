"""Pump Soap Bottle.

Plan: Centerline extremes (8,4)-(40,44); VRECT_L keyshape supports the complete standalone source silhouette.
Construction: Lucide soap-dispenser-droplet: rounded bottle and dispensing stem. Preserve the blank source face and left spout; omit extra decoration.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ffeedc1-7b0e-428e-9f85-7eaa08e554a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/soap 1_6ffeedc1-7b0e-428e-9f85-7eaa08e554a9.svg'
AUTHOR = "gpt-6"

class Batch04Icon7(Solo48):
    icon_id = 'pump-soap-bottle-6ffeedc1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('pump-soap-bottle',)
    keywords = ('pump', 'soap', 'bottle')

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
        path("body",(14,18),[("L",(18,18)),("L",(18,14)),("L",(24,14)),("L",(30,14)),("L",(30,18)),("L",(34,18)),("A",(40,24),6,6,True),("L",(40,38)),("A",(34,44),6,6,True),("L",(14,44)),("A",(8,38),6,6,True),("L",(8,24)),("A",(14,18),6,6,True)],True)
        self.add_line("stem",(24,4),(24,14));self.relate("connect","stem","body")
        self.add_polyline("pump",(8,10),(14,4),(24,4),(32,4));self.relate("connect","pump","stem")
