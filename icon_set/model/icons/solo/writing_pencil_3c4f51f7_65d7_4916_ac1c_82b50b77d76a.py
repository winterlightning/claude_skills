"""Writing Pencil.
Plan: SQUARE, centerline extremes (6,6)-(42,42); standalone complete source concept.
Construction and reduction: Lucide pencil informs parallel barrel, broad triangular point and rounded upper end. Source tip seam retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3c4f51f7-65d7-4916-ac1c-82b50b77d76a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/content pen_3c4f51f7-65d7-4916-ac1c-82b50b77d76a.svg'
AUTHOR = "gpt-6"
class Batch06Icon14(Solo48):
    icon_id = 'writing-pencil-3c4f51f7'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ()
    keywords = ('writing', 'pencil')
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
        path("pencil",(6,42),[("L",(12,28)),("L",(30,10)),("C",(36,6),(32,8),(33,6)),("A",(42,12),6,6,True),("C",(38,18),(42,15),(40,16)),("L",(20,36)),("L",(6,42))],True)
        self.add_line("tip",(12,28),(20,36));self.relate("connect","tip","pencil")
