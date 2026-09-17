"""Person Reading Newspaper.
Plan: VRECT_L, centerline extremes (8,4)-(40,44); standalone complete source concept.
Construction and reduction: Human user.svg and full_body_ref.png own circular head and smooth shoulders. Head center24,10 radius6; shoulders y24 give exactly8 centerline /4 ink gap. Lucide book-open informs newspaper fold. Tiny writing marks omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'babe57e9-dadd-4de6-bc23-187db177304c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/newspaper read_babe57e9-dadd-4de6-bc23-187db177304c.svg'
AUTHOR = "gpt-6"
class Batch06Icon9(Solo48):
    icon_id = 'person-reading-newspaper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ()
    keywords = ('person', 'reading', 'newspaper')
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
        circle("head",24,10,6)
        path("shoulders",(16,31),[("L",(16,28)),("A",(20,24),4,4,True),("L",(28,24)),("A",(32,28),4,4,True),("L",(32,31))])
        self.add_polyline("paper",(8,28),(16,31),(24,34),(32,31),(40,28),(40,40),(24,44),(8,40),closed=True)
        self.add_line("fold",(24,34),(24,44));self.relate("connect","fold","paper");self.relate("connect","shoulders","paper")
