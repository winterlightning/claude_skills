"""Soap Dispenser Bottle.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide soap-dispenser-droplet informs rounded body. Source-specific detached head remains separated by at least8 centerline units; no extra droplet.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '726d1a97-a34c-466f-a137-80c846bfc822'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/soap_726d1a97-a34c-466f-a137-80c846bfc822.svg'
AUTHOR = "gpt-6"
class Batch05Icon4(Solo48):
    icon_id = 'soap-dispenser-bottle-726d1a97'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/soap"
    aliases = ('soap-dispenser-bottle',)
    keywords = ('soap', 'dispenser', 'bottle')
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
        axis=24
        path("body",(14,20),[("L",(16,20)),("L",(20,14)),("L",(28,14)),("L",(32,20)),("L",(34,20)),("A",(40,26),6,6,True),("L",(40,38)),("A",(34,44),6,6,True),("L",(14,44)),("A",(8,38),6,6,True),("L",(8,26)),("A",(14,20),6,6,True)],True)
        path("head",(10,8),[("L",(12,6)),("C",(18,4),(14,4),(16,4)),("L",(32,4))])
