"""Lidded Trash Bin.

Plan: Mirrored body, radius4 corners, centered handle. Bounds (8,4)-(40,44).
Construction: Lucide trash: blank body with rounded base, projecting lid and integrated handle.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65c50ba7-cc47-43de-89c0-2b01580da7ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/trash_65c50ba7-cc47-43de-89c0-2b01580da7ac.svg'
AUTHOR = "gpt-6"

class Batch03Icon11(Solo48):
    icon_id = 'lidded-trash-bin-65c50ba7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/trash"
    aliases = ('lidded-trash-bin',)
    keywords = ('lidded', 'trash', 'bin')

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
        self.add_polyline("lid",(8,12),(12,12),(16,12),(32,12),(36,12),(40,12))
        path("body",(12,12),[("L",(12,40)),("A",(16,44),4,4,False),("L",(32,44)),("A",(36,40),4,4,False),("L",(36,12))])
        path("handle",(16,12),[("L",(16,8)),("A",(20,4),4,4,True),("L",(28,4)),("A",(32,8),4,4,True),("L",(32,12))])
        self.relate("connect","lid","body");self.relate("connect","lid","handle")
