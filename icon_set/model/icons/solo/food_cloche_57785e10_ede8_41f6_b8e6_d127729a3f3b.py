"""Food Cloche.

Plan: Symmetric cover with radius6 shoulders, radius8 handle and radius4 tray corners. Bounds (6,6)-(42,42).
Construction: Lucide concierge-bell: cover meeting a low tray; retain the original arched handle and tall cover.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57785e10-ede8-41f6-b8e6-d127729a3f3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/cage_57785e10-ede8-41f6-b8e6-d127729a3f3b.svg'
AUTHOR = "gpt-6"

class Batch03Icon0(Solo48):
    icon_id = 'food-cloche-57785e10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/cloche"
    aliases = ('food-cloche',)
    keywords = ('food', 'cloche')

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
        path("cover",(8,34),[("L",(10,20)),("A",(16,14),6,6,True),("L",(32,14)),("A",(38,20),6,6,True),("L",(40,34))])
        path("handle",(16,14),[("A",(32,14),8,8,True)])
        self.relate("connect","cover","handle")
        path("tray",(6,34),[("L",(8,34)),("L",(40,34)),("L",(42,34)),("L",(42,38)),("A",(38,42),4,4,True),("L",(10,42)),("A",(6,38),4,4,True),("L",(6,34))],True)
        self.relate("connect","tray","cover")
