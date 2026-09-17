"""Hand Holding Smartphone.

Plan: One thumb occludes the right device edge; upper knuckles and lower palm remain naturally asymmetric. Bounds (6,6)-(42,42). Omit the bottom screen separator to prevent crowding the palm.
Construction: Lucide smartphone supplies the rounded device. The supplied reference owns the gripping hand; shared human references informed simple anatomy, with no head/body gap applicable.
Reduction: Preserve the complete physical subject; no decorative content added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e036fe0-db92-45bb-bf16-7ea8c0a3fcfa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/mobilephone hold_5e036fe0-db92-45bb-bf16-7ea8c0a3fcfa.svg'
AUTHOR = "gpt-6"

class Batch03Icon7(Solo48):
    icon_id = 'hand-holding-smartphone-5e036fe0'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/phone"
    aliases = ('hand-holding-smartphone',)
    keywords = ('hand', 'holding', 'smartphone')

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
        path("phone",(28,24),[("L",(28,12)),("L",(28,10)),("A",(24,6),4,4,False),("L",(10,6)),("A",(6,10),4,4,False),("L",(6,38)),("A",(10,42),4,4,False),("L",(24,42)),("A",(28,38),4,4,False),("L",(28,32))])
        path("thumb-palm",(32,24),[("L",(28,24)),("L",(24,24)),("A",(24,32),4,4,False),("L",(28,32)),("C",(38,40),(28,37),(33,40)),("L",(42,40))])
        self.relate("connect","phone","thumb-palm")
        path("hand-back",(28,12),[("L",(32,12)),("C",(42,18),(36,12),(38,18))])
        self.relate("connect","phone","hand-back")
