"""Rakhi Bracelet Ornament.

Plan: Teardrop jewel on horizontal bracelet thread with pendant cord. Axis24, bounds (6,6)-(42,42).
Construction: Source pointed ornament; circular jewel centered within symmetrical curved casing.
Reduction: Thread bundle reduced to one stroke per direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '4ed5443a-ff9e-457c-b4f2-1e7ee3e1718d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/raksha bandhan_4ed5443a-ff9e-457c-b4f2-1e7ee3e1718d.svg'
AUTHOR = 'gpt-6'


class IconRakhiBraceletOrnament(Solo48):
    icon_id = 'rakhi-bracelet-ornament'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('rakhi', 'bracelet', 'ornament')

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
        path('ornament',(24,6),[('C',(36,26),(28,12),(36,16)),('A',(24,38),12,12,True),('A',(12,26),12,12,True),('C',(24,6),(12,16),(20,12))],True)
        circle('jewel',24,25,3)
        for name,a,b in [('left',(6,26),(12,26)),('right',(36,26),(42,26)),('drop',(24,38),(24,42))]:self.add_line(name,a,b);self.relate('connect',name,'ornament')
