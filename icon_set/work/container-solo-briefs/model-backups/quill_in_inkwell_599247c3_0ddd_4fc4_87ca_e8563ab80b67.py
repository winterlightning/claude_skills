"""Quill in Inkwell.
Plan: SQUARE, centerline extremes (6,6)-(42,42); standalone complete source concept.
Construction and reduction: Lucide feather informs pointed quill with a shaft. Original source supplies joined inkwell. Small secondary vein omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '599247c3-0ddd-4fc4-87ca-e8563ab80b67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/quill ink_599247c3-0ddd-4fc4-87ca-e8563ab80b67.svg'
AUTHOR = "gpt-6"
class Batch06Icon10(Solo48):
    icon_id = 'quill-in-inkwell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ()
    keywords = ('quill', 'in', 'inkwell')
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
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[("L",(r-rad,t)),("A",(r,t+rad),rad,rad,True),("L",(r,b-rad)),("A",(r-rad,b),rad,rad,True),("L",(l+rad,b)),("A",(l,b-rad),rad,rad,True),("L",(l,t+rad)),("A",(l+rad,t),rad,rad,True)],True)
        def openbook(top=8,bottom=40):
            axis=24
            for side in (-1,1):
                p=lambda x,y:(axis+side*x,y)
                path(f"page-{side}",p(0,top+4),[("C",p(20,top),p(7,top),p(13,top)),("L",p(20,bottom-4)),("C",p(0,bottom),p(12,bottom-4),p(7,bottom-4)),("L",p(0,top+4))],True)
            self.relate("connect","page--1","page-1")
        path("bottle",(12,30),[("L",(12,28)),("L",(20,28)),("L",(28,28)),("L",(28,30)),("A",(34,36),6,6,True),("L",(34,42)),("L",(6,42)),("L",(6,36)),("A",(12,30),6,6,True)],True)
        path("feather",(24,20),[("C",(42,6),(24,12),(34,6)),("C",(24,20),(42,16),(34,20))],True)
        self.add_polyline("shaft",(20,28),(24,20),(32,14));self.relate("connect","shaft","bottle");self.relate("connect","shaft","feather")
