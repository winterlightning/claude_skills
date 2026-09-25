"""Open Book with Curved Lines.
Plan: HRECT_L, centerline extremes (4,8)-(44,40); standalone complete source concept.
Construction and reduction: Lucide book-open-text: mirrored curved pages and one curved mark on each. Secondary backing omitted to prioritize the marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '501f68f9-2918-51e9-a90d-9cd08d40aaa2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/book open text_501f68f9-2918-51e9-a90d-9cd08d40aaa2.svg'
AUTHOR = "gpt-6"
class Batch06Icon2(Solo48):
    icon_id = 'open-book-with-curved-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ()
    keywords = ('open', 'book', 'with', 'curved', 'lines')
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
        openbook()
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            path(f"writing-{side}",p(9,23),[("C",p(11,22),p(9,22),p(10,22))])
