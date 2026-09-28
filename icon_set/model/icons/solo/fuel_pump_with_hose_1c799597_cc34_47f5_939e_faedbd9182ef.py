"""Fuel Pump.

Plan: Body x6..30, hose reaches42. Bounds (6,6)-(42,42). Drop the narrow secondary nozzle grip line.
Construction: Lucide fuel: rounded dispenser, connected hose and angled nozzle. Keep the supplied short display mark.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c799597-cc34-47f5-939e-faedbd9182ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/gas pump 1_1c799597-cc34-47f5-939e-faedbd9182ef.svg'
AUTHOR = "gpt-6"

class Batch03Icon2(Solo48):
    icon_id = 'fuel-pump-with-hose-1c799597'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('fuel-pump-with-hose',)
    keywords = ('fuel', 'pump', 'with', 'hose')

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
        path("body",(10,6),[("L",(26,6)),("A",(30,10),4,4,True),("L",(30,32)),("L",(30,38)),("A",(26,42),4,4,True),("L",(10,42)),("A",(6,38),4,4,True),("L",(6,10)),("A",(10,6),4,4,True)],True)
        self.add_line("display",(15,15),(21,15))
        path("hose",(30,32),[("L",(36,32)),("A",(42,26),6,6,False),("L",(42,16)),("L",(38,12))])
        self.relate("connect","body","hose")
