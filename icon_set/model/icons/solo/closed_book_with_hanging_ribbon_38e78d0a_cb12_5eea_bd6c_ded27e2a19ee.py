"""Closed Book with Hanging Ribbon.
Plan: VRECT_L, centerline bounds (8,4)-(40,44), complete standalone subject.
Construction: Lucide book and book-marked inform the rounded page block and ribbon. Right-hanging ribbon interrupts the page edge; source spine strip retained.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '38e78d0a-cb12-5eea-bd6c-ded27e2a19ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/book close bookmark_38e78d0a-cb12-5eea-bd6c-ded27e2a19ee.svg'
AUTHOR = "gpt-6"
class Batch05Icon11(Solo48):
    icon_id = 'closed-book-with-hanging-ribbon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hanging"
    aliases = ('closed-book-with-hanging-ribbon',)
    keywords = ('closed', 'book', 'with', 'hanging', 'ribbon')
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
        path("cover",(12,4),[("L",(17,4)),("L",(40,4)),("L",(40,32)),("L",(32,32)),("L",(22,32)),("L",(17,32)),("L",(12,32)),("A",(8,36),4,4,False),("L",(8,8)),("A",(12,4),4,4,True)],True)
        self.add_line("spine",(17,4),(17,32));self.relate("connect","cover","spine")
        path("pages-left",(8,36),[("A",(12,40),4,4,False),("L",(22,40))])
        self.add_polyline("pages-right",(32,40),(40,40),(40,32))
        self.add_polyline("ribbon",(22,32),(22,40),(22,44),(27,40),(32,44),(32,40),(32,32))
        for a,b in [("cover","pages-left"),("cover","pages-right"),("cover","ribbon"),("ribbon","pages-left"),("ribbon","pages-right")]:self.relate("connect",a,b)
