"""Smartphone Storefront.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide store and smartphone inform scalloped awning and rounded phone. Four equal panels; omit narrow roof stripe divisions to keep the top open.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e834be15-3882-4454-8a14-9631e638a9a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/mobile shop 1_e834be15-3882-4454-8a14-9631e638a9a5.svg'
AUTHOR = "gpt-6"
class Batch05Icon2(Solo48):
    icon_id = 'smartphone-storefront-e834be15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/store"
    aliases = ('smartphone-storefront',)
    keywords = ('smartphone', 'storefront')
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
        path("roof",(8,14),[("L",(8,10)),("A",(14,4),6,6,True),("L",(34,4)),("A",(40,10),6,6,True),("L",(40,14))])
        for i,cx in enumerate((12,20,28,36)):
            k=f"scallop-{i}";path(k,(cx-4,14),[("A",(cx,18),4,4,False),("A",(cx+4,14),4,4,False)])
            if i:self.relate("connect",k,f"scallop-{i-1}")
        self.relate("connect","roof","scallop-0");self.relate("connect","roof","scallop-3")
        path("phone",(12,18),[("L",(12,36)),("L",(12,40)),("A",(16,44),4,4,False),("L",(32,44)),("A",(36,40),4,4,False),("L",(36,36)),("L",(36,18))])
        self.relate("connect","phone","scallop-0");self.relate("connect","phone","scallop-3")
        self.add_line("bezel",(12,36),(36,36));self.relate("connect","phone","bezel")
