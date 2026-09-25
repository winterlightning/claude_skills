"""Closed Hardcover Book.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide book informs the round lower spine. Source-specific inward fore-edge and left spine strip retained; empty cover.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b25bbd5-4957-5981-b8e7-ad2f1592fd4c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/book library_0b25bbd5-4957-5981-b8e7-ad2f1592fd4c.svg'
AUTHOR = "gpt-6"
class Batch05Icon12(Solo48):
    icon_id = 'closed-hardcover-book-reference'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ('closed-hardcover-book-reference',)
    keywords = ('closed', 'hardcover', 'book', 'reference')
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
        path("cover",(14,4),[("L",(17,4)),("L",(40,4)),("L",(40,34)),("L",(17,34)),("L",(13,34)),("A",(8,39),5,5,False),("L",(8,10)),("A",(14,4),6,6,True)],True)
        self.add_line("spine",(17,4),(17,34));self.relate("connect","cover","spine")
        path("pages",(8,39),[("A",(13,44),5,5,False),("L",(40,44)),("C",(40,34),(38,41),(38,37))]);self.relate("connect","pages","cover")
