"""Book with Upper Bookmark.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide book-marked informs the upper forked ribbon and rounded page block. Spine strip omitted to prioritize clear upper ribbon and fore-edge.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f63c61b-e53d-5cde-8728-b0a9e4894ff4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/book bookmark_6f63c61b-e53d-5cde-8728-b0a9e4894ff4.svg'
AUTHOR = "gpt-6"
class Batch05Icon9(Solo48):
    icon_id = 'book-with-upper-bookmark'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ('book-with-upper-bookmark',)
    keywords = ('book', 'with', 'upper', 'bookmark')
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
        path("cover",(14,4),[("L",(16,4)),("L",(24,4)),("L",(32,4)),("L",(40,4)),("L",(40,34)),("L",(16,34)),("L",(13,34)),("A",(8,39),5,5,False),("L",(8,10)),("A",(14,4),6,6,True)],True)
        path("pages",(8,39),[("A",(13,44),5,5,False),("L",(40,44)),("L",(40,34))]);self.relate("connect","pages","cover")
        self.add_polyline("ribbon",(24,4),(24,18),(28,14),(32,18),(32,4));self.relate("connect","cover","ribbon")
