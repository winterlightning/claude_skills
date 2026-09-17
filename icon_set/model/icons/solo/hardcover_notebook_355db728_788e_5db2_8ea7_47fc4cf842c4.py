"""Hardcover Notebook.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide book informs rounded cover and curved bottom page block. Original owns left spine strip. Broad corners and blank cover preserved.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '355db728-788e-5db2-8ea7-47fc4cf842c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/notes diary_355db728-788e-5db2-8ea7-47fc4cf842c4.svg'
AUTHOR = "gpt-6"
class Batch05Icon14(Solo48):
    icon_id = 'hardcover-notebook'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/notebook"
    aliases = ('hardcover-notebook',)
    keywords = ('hardcover', 'notebook')
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
        path("cover",(14,4),[("L",(17,4)),("L",(34,4)),("A",(40,10),6,6,True),("L",(40,34)),("L",(40,38)),("A",(34,44),6,6,True),("L",(14,44)),("A",(8,38),6,6,True),("L",(8,34)),("L",(8,10)),("A",(14,4),6,6,True)],True)
        self.add_polyline("seam",(8,34),(17,34),(34,34),(40,34));self.relate("connect","cover","seam")
        self.add_line("spine",(17,4),(17,34));self.relate("connect","spine","cover");self.relate("connect","spine","seam")
