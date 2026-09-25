"""Open Book with Turning Page.
Plan: SQUARE, centerline extremes (6,6)-(42,42); standalone complete source concept.
Construction and reduction: Lucide book-open informs continuous page contours. Original owns the raised right sheet; asymmetry is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a8cb8ea-8874-5376-aa01-1d5cb4dfa804'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/book next page_7a8cb8ea-8874-5376-aa01-1d5cb4dfa804.svg'
AUTHOR = "gpt-6"
class Batch06Icon4(Solo48):
    icon_id = 'open-book-with-turning-page'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    categories = ("primitives", "content")
    aliases = ()
    keywords = ('open', 'book', 'with', 'turning', 'page')
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
        path("left",(24,14),[("C",(6,10),(18,10),(12,10)),("L",(6,38)),("C",(24,42),(12,38),(18,38)),("L",(24,14))],True)
        path("turning",(24,14),[("C",(34,6),(27,9),(30,6)),("L",(34,16)),("L",(34,32)),("C",(24,42),(30,34),(27,38)),("L",(24,14))],True)
        self.add_polyline("under-page",(34,16),(42,16),(42,40),(24,42))
        # Split the raised sheet at its attachment to the underlying sheet.
        self.relate("connect","turning","under-page");self.relate("connect","left","turning");self.relate("connect","left","under-page")
