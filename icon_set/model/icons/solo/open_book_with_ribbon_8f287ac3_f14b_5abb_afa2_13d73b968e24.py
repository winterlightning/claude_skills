"""Open Book with Ribbon.
Plan: HRECT_L, centerline extremes (4,8)-(44,40); standalone complete source concept.
Construction and reduction: Lucide book-open and book-marked: page pair with a right upper ribbon. Central fold shifted left to make ribbon room; tiny bottom crease omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8f287ac3-f14b-5abb-afa2-13d73b968e24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/book open bookmark_8f287ac3-f14b-5abb-afa2-13d73b968e24.svg'
AUTHOR = "gpt-6"
class Batch06Icon3(Solo48):
    icon_id = 'open-book-with-ribbon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ()
    keywords = ('open', 'book', 'with', 'ribbon')
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
        path("left",(18,12),[("C",(4,8),(14,8),(9,8)),("L",(4,36)),("C",(18,40),(9,36),(14,36)),("L",(18,12))],True)
        path("right",(18,12),[("C",(26,8),(21,9),(23,8)),("L",(34,8)),("L",(40,8)),("A",(44,12),4,4,True),("L",(44,32)),("A",(40,36),4,4,True),("C",(18,40),(30,36),(23,37)),("L",(18,12))],True)
        self.relate("connect","left","right")
        self.add_polyline("ribbon",(26,8),(26,22),(30,18),(34,22),(34,8));self.relate("connect","ribbon","right")
