"""Gas Station Pump.

Plan: Body x6..32, rectangular display with 9u side margins and attached hose. Bounds (6,6)-(42,42). Simplify nozzle grip to one continuous stroke.
Construction: Lucide fuel: rounded dispenser and hose; supplied reference owns the rectangular display.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6ad2876-4c17-480f-888d-091722c8b41f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/gas pump_c6ad2876-4c17-480f-888d-091722c8b41f.svg'
AUTHOR = "gpt-6"

class Batch03Icon6(Solo48):
    icon_id = 'fuel-pump-with-display-c6ad2876'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('fuel-pump-with-display',)
    keywords = ('fuel', 'pump', 'with', 'display')

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
        path("body",(10,6),[("L",(28,6)),("A",(32,10),4,4,True),("L",(32,32)),("L",(32,38)),("A",(28,42),4,4,True),("L",(10,42)),("A",(6,38),4,4,True),("L",(6,10)),("A",(10,6),4,4,True)],True)
        self.add_polyline("display",(15,15),(23,15),(23,23),(15,23),closed=True)
        path("hose",(32,32),[("L",(36,32)),("A",(42,26),6,6,False),("L",(42,16)),("L",(38,12))])
        self.relate("connect","body","hose")
