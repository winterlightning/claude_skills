"""Cylindrical Can.

Plan: Top ellipse rx16 ry6 at (24,10); straight walls and matching lower half ellipse. Centerline bounds (8,4)-(40,44).
Construction: Lucide cylinder: shared elliptical rim and vertical walls; enlarge rim depth to preserve its opening at stroke4.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e67fccd5-f1b8-43e8-b6fa-2029a8db8a07'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/can 1_e67fccd5-f1b8-43e8-b6fa-2029a8db8a07.svg'
AUTHOR = "gpt-6"

class Batch02Icon7(Solo48):
    icon_id = 'cylindrical-tin-can-e67fccd5'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('cylindrical-tin-can',)
    keywords = ('cylindrical', 'tin', 'can')

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
        cx, rx, ry = 24, 16, 6
        left,right=cx-rx,cx+rx
        path("body",(left,10),[("A",(right,10),rx,ry,True),("L",(right,38)),("A",(left,38),rx,ry,True),("L",(left,10))],True)
        path("rim-front",(right,10),[("A",(left,10),rx,ry,True)])
        self.relate("connect","body","rim-front")
