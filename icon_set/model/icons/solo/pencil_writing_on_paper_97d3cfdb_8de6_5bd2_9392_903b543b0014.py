"""Pencil Writing on Paper.
Plan: SQUARE, centerline extremes (6,6)-(42,42); standalone complete source concept.
Construction and reduction: Lucide file-pen-line and pencil inform a pencil overlapping a paper edge. Omit writing marks and tiny cap seam for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97d3cfdb-8de6-5bd2-9392-903b543b0014'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/content pen_97d3cfdb-8de6-5bd2-9392-903b543b0014.svg'
AUTHOR = "gpt-6"
class Batch06Icon7(Solo48):
    icon_id = 'pencil-writing-on-paper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ()
    keywords = ('pencil', 'writing', 'on', 'paper')
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
        path("paper",(22,6),[("L",(10,6)),("A",(6,10),4,4,False),("L",(6,38)),("A",(10,42),4,4,False),("L",(34,42)),("A",(38,38),4,4,False),("L",(38,30))])
        self.add_polyline("pencil",(20,28),(24,16),(34,6),(42,14),(32,24),(20,28))
        self.add_line("tip-seam",(24,16),(32,24));self.relate("connect","pencil","tip-seam")
