"""Smartphone with Flash.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide smartphone informs rounded device. Original owns radiating front-camera light and interrupted top edge; reduce rays to three to preserve clearance.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '29b668a7-57ab-4309-b2ab-d6101e735bf2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/phone selfie_29b668a7-57ab-4309-b2ab-d6101e735bf2.svg'
AUTHOR = "gpt-6"
class Batch05Icon3(Solo48):
    icon_id = 'smartphone-with-flash-29b668a7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('smartphone-with-flash',)
    keywords = ('smartphone', 'with', 'flash')
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
        path("phone",(12,16),[("A",(8,20),4,4,False),("L",(8,26)),("L",(8,40)),("A",(12,44),4,4,False),("L",(36,44)),("A",(40,40),4,4,False),("L",(40,26)),("L",(40,20)),("A",(36,16),4,4,False)])
        self.add_line("bezel",(8,26),(40,26));self.relate("connect","phone","bezel")
        self.add_line("ray-top",(axis,4),(axis,10))
        for side in (-1,1):self.add_line(f"ray-{side}",(axis+side*12,4),(axis+side*8,8))
