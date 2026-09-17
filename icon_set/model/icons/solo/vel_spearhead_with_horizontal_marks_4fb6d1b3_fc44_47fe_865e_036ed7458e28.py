"""Vel Spearhead with Horizontal Marks.

Plan: Symmetric pointed spearhead with horizontal ritual marks and foot. Bounds (8,4)-(40,44).
Construction: Source Vel leaf-shaped outline; no exact local Lucide match.
Reduction: Two horizontal marks replace three interrupted lines; base notch and separate foot omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '4fb6d1b3-fc44-47fe-865e-036ed7458e28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/thaipusam_4fb6d1b3-fc44-47fe-865e-036ed7458e28.svg'
AUTHOR = 'gpt-6'


class IconVelSpearheadWithHorizontalMarks(Solo48):
    icon_id = 'vel-spearhead-with-horizontal-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('vel', 'spearhead', 'with', 'horizontal', 'marks')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('head',(24,4),[('C',(40,26),(30,12),(40,18)),('C',(24,38),(40,33),(32,38)),('C',(8,26),(16,38),(8,33)),('C',(24,4),(8,18),(18,12))],True)
        self.add_line('mark-a',(21,20),(27,20));self.add_line('mark-b',(21,28),(27,28))
        self.add_line('stem',(24,38),(24,44));self.relate('connect','stem','head')
