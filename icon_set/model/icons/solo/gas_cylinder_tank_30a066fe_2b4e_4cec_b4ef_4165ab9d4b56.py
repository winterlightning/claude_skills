"""Gas Cylinder.

Plan: Mirrored radius10 shoulders, radius8 base corners and neck12 wide. Bounds (8,4)-(40,44).
Construction: Lucide heater supports rounded structural body construction; the source owns the cylinder neck and cap.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30a066fe-2b4e-4cec-b4ef-4165ab9d4b56'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/gas 1_30a066fe-2b4e-4cec-b4ef-4165ab9d4b56.svg'
AUTHOR = "gpt-6"

class Batch03Icon4(Solo48):
    icon_id = 'gas-cylinder-tank-30a066fe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('gas-cylinder-tank',)
    keywords = ('gas', 'cylinder', 'tank')

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
        path("tank",(18,14),[("L",(30,14)),("A",(40,24),10,10,True),("L",(40,36)),("A",(32,44),8,8,True),("L",(16,44)),("A",(8,36),8,8,True),("L",(8,24)),("A",(18,14),10,10,True)],True)
        self.add_polyline("cap",(14,4),(18,4),(30,4),(34,4))
        for side in (-1,1):
            name=f"neck-{side}";x=axis+side*6
            self.add_line(name,(x,4),(x,14))
            self.relate("connect",name,"tank")
            self.relate("connect",name,"cap")
