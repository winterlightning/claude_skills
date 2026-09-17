"""Book with Lower Bookmark.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide book and book-marked inform page block and forked ribbon. Original owns the left-hanging ribbon and short cover mark.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1396bfae-fe02-4eec-8b62-f65cf84850c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/repo_1396bfae-fe02-4eec-8b62-f65cf84850c4.svg'
AUTHOR = "gpt-6"
class Batch05Icon8(Solo48):
    icon_id = 'book-with-lower-bookmark'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/lower"
    aliases = ('book-with-lower-bookmark',)
    keywords = ('book', 'with', 'lower', 'bookmark')
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
        path("cover",(12,4),[("L",(40,4)),("L",(40,32)),("L",(26,32)),("L",(16,32)),("L",(12,32)),("A",(8,36),4,4,False),("L",(8,8)),("A",(12,4),4,4,True)],True)
        path("pages-left",(8,36),[("A",(12,40),4,4,False),("L",(16,40))])
        self.add_polyline("pages-right",(26,40),(40,40),(40,32))
        self.add_polyline("ribbon",(16,32),(16,40),(16,44),(21,40),(26,44),(26,40),(26,32))
        self.add_line("cover-mark",(18,14),(18,22))
        for a,b in [("cover","pages-left"),("cover","pages-right"),("cover","ribbon"),("ribbon","pages-left"),("ribbon","pages-right")]:self.relate("connect",a,b)
