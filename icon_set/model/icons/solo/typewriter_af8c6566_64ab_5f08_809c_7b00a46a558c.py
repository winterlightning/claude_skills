"""Typewriter.
Plan: SQUARE, centerline extremes (6,6)-(42,42); standalone complete source concept.
Construction and reduction: Lucide keyboard informs repeated key marks. Paper, carriage and sloping body define source typewriter. Two sparse key rows, shared spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af8c6566-64ab-5f08-809c-7b00a46a558c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/content typing machine_af8c6566-64ab-5f08-809c-7b00a46a558c.svg'
AUTHOR = "gpt-6"
class Batch06Icon11(Solo48):
    icon_id = 'typewriter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ()
    keywords = ('typewriter',)
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
        self.add_polyline("paper",(16,17),(16,6),(32,6),(32,17))
        self.add_polyline("carriage",(6,14),(6,17),(12,17),(16,17),(32,17),(36,17),(42,17));self.relate("connect","paper","carriage")
        path("body",(12,17),[("L",(6,38)),("A",(10,42),4,4,False),("L",(38,42)),("A",(42,38),4,4,False),("L",(36,17))]);self.relate("connect","body","carriage")
        for y in (25,33):
            for x in (20,28):self.add_dot(f"key-{x}-{y}",(x,y))
