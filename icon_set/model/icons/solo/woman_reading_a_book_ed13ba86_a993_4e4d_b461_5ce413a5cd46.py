"""Woman Reading a Book.
Plan: SQUARE, centerline extremes (6,6)-(42,42); standalone complete source concept.
Construction and reduction: Human user.svg and full_body_ref.png guide circular head and simplified hands. Source owns hair and book interaction; no exposed torso. Lucide book-open informs folded pages.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed13ba86-a993-4e4d-b461-5ce413a5cd46'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/newspaper read woman_ed13ba86-a993-4e4d-b461-5ce413a5cd46.svg'
AUTHOR = "gpt-6"
class Batch06Icon12(Solo48):
    icon_id = 'woman-reading-a-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ()
    keywords = ('woman', 'reading', 'a', 'book')
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
        circle("face",24,12,6)
        for side in (-1,1):
            x=24+side*6;path(f"hair-{side}",(x,12),[("C",(24+side*8,26),(x,18),(24+side*8,20)),("L",(x,28))]);self.relate("connect","face",f"hair-{side}")
        self.add_polyline("book-top",(10,30),(10,26),(18,28),(24,30),(30,28),(38,26),(38,30))
        self.add_polyline("book-bottom",(10,38),(10,40),(24,42),(38,40),(38,38))
        self.add_line("fold",(24,30),(24,42));self.relate("connect","fold","book-top");self.relate("connect","fold","book-bottom")
        for side in (-1,1):
            k=f"hand-{side}";x=24+side*14;path(k,(x,30),[("A",(x+side*4,34),4,4,side<0),("A",(x,38),4,4,side<0)])
            self.relate("connect",k,"book-top");self.relate("connect",k,"book-bottom");self.relate("connect",f"hair-{side}","book-top")
