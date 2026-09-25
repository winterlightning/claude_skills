"""Canopy Tent with Curtains.

Plan: Mirrored roof and gathered drapes around axis24. Centerline bounds (6,6)-(42,42).
Construction: Lucide tent: common peak and paired supports; supplied reference owns the event-canopy curtains.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c277800-7ab9-4394-bd17-3f7b22de16b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/tent_8c277800-7ab9-4394-bd17-3f7b22de16b8.svg'
AUTHOR = "gpt-6"

class Batch02Icon1(Solo48):
    icon_id = 'canopy-tent-with-curtains-8c277800'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('canopy-tent-with-curtains',)
    keywords = ('canopy', 'tent', 'with', 'curtains')

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
        axis = 24
        self.add_polyline("roof",(6,18),(axis,6),(42,18),(32,18),(16,18),(6,18))
        for side in (-1,1):
            p=lambda x,y:(axis+side*x,y)
            name=f"curtain-{side}"
            path(name,p(18,18),[("L",p(18,32)),("L",p(18,42)),("L",p(8,42)),("C",p(18,32),p(8,38),p(12,34)),("C",p(8,18),p(10,29),p(8,24))])
            self.relate("connect",name,"roof")
