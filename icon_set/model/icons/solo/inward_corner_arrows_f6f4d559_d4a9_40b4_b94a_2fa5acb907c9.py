"""Inward Corner Arrows.
Plan: Four identical diagonal arrows around a rounded center square, mirrored about both axes. Extremes (6,6)-(42,42).
Construction reference: local Lucide minimize-2, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f6f4d559-d4a9-40b4-b94a-2fa5acb907c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/shrink_f6f4d559-d4a9-40b4-b94a-2fa5acb907c9.svg'
AUTHOR = 'gpt-6'

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+"-top",(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+"-bottom",(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+"-top",name+"-bottom",closed=True)

def path(icon,name,start,commands,closed=False):
    point=start;members=[]
    for i,command in enumerate(commands):
        member=f"{name}-{i}"; kind=command[0]; end=command[-1]
        if kind=="L":icon.add_line(member,point,end)
        elif kind=="A":icon.add_arc(member,point,end,radius_x=command[1],radius_y=command[2],sweep=command[3])
        else:icon.add_bezier(member,point,(command[1],command[2],end))
        members.append(member);point=end
    icon.add_contour(name,*members,closed=closed)

class Drawing(Solo48):
    icon_id = 'inward-corner-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('arrows', 'inward', 'shrink', 'resize', 'square', 'corners')
    def build(self):
        for sx in (-1,1):
            for sy in (-1,1):
                p=lambda x,y:(24+sx*x,24+sy*y)
                name=f"arrow-{sx}-{sy}"
                self.add_polyline(name+"-head",p(18,10),p(10,10),p(10,18))
                self.add_line(name+"-shaft",p(18,18),p(10,10))
                self.relate("connect",name+"-head",name+"-shaft")
        path(self,"center",(22,20),[("L",(26,20)),("A",2,2,True,(28,22)),("L",(28,26)),("A",2,2,True,(26,28)),("L",(22,28)),("A",2,2,True,(20,26)),("L",(20,22)),("A",2,2,True,(22,20))],True)
