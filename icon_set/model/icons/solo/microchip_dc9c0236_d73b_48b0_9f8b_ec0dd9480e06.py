"""Microchip.

Plan: Centerline extremes (6,6)-(42,42); SQUARE keyshape supports the complete standalone source silhouette.
Construction: Lucide microchip: rounded blank package and repeated pins. Two pins per edge preserve the supplied reference.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc9c0236-d73b-48b0-9f8b-ec0dd9480e06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/chip_dc9c0236-d73b-48b0-9f8b-ec0dd9480e06.svg'
AUTHOR = "gpt-6"

class Batch04Icon1(Solo48):
    icon_id = 'microchip-dc9c0236'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('microchip',)
    keywords = ('microchip',)

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
        path("body",(16,12),[("L",(18,12)),("L",(30,12)),("L",(32,12)),("A",(36,16),4,4,True),("L",(36,18)),("L",(36,30)),("L",(36,32)),("A",(32,36),4,4,True),("L",(30,36)),("L",(18,36)),("L",(16,36)),("A",(12,32),4,4,True),("L",(12,30)),("L",(12,18)),("L",(12,16)),("A",(16,12),4,4,True)],True)
        for i,p in enumerate((18,30)):
            for side,a,b in [("top",(p,12),(p,6)),("bottom",(p,36),(p,42)),("left",(12,p),(6,p)),("right",(36,p),(42,p))]:
                k=f"pin-{side}-{i}";self.add_line(k,a,b);self.relate("connect","body",k)
