"""Notebook and Pencil.
Plan: HRECT_L, centerline extremes (4,8)-(44,40); standalone complete source concept.
Construction and reduction: Lucide notebook-pen and pencil inform the natural stationery pair. Preserve upright separate pencil; omit notebook label and spine to keep the narrow cover clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d9b4e4c-8655-4e86-8918-1cfc2f4b616b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/notebook pencil_1d9b4e4c-8655-4e86-8918-1cfc2f4b616b.svg'
AUTHOR = "gpt-6"
class Batch06Icon1(Solo48):
    icon_id = 'notebook-and-pencil'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ()
    keywords = ('notebook', 'and', 'pencil')
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
        box("notebook",4,8,27,40)
        path("pencil",(36,16),[("L",(40,8)),("L",(44,16)),("L",(44,36)),("A",(40,40),4,4,True),("A",(36,36),4,4,True),("L",(36,16))],True)
