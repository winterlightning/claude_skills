"""Move Item Down Diagram.
Plan: Two equal rounded nodes, detached connector and bowed downward arrow. Extremes (8,4)-(40,44).
Construction reference: local Lucide move-down, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '056b3d0c-fcc3-411e-a2dc-152ac0a8d690'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/move to bottom_056b3d0c-fcc3-411e-a2dc-152ac0a8d690.svg'
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

def box(icon,name,x,y,w,h,r=2):
    path(icon,name,(x+r,y),[("L",(x+w-r,y)),("A",r,r,True,(x+w,y+r)),("L",(x+w,y+h-r)),("A",r,r,True,(x+w-r,y+h)),("L",(x+r,y+h)),("A",r,r,True,(x,y+h-r)),("L",(x,y+r)),("A",r,r,True,(x+r,y))],True)

class Drawing(Solo48):
    icon_id = 'move-item-down-diagram'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('move', 'down', 'nodes', 'diagram', 'reorder', 'arrow')
    def build(self):
        for y in (4,36):box(self,"node-"+str(y),8,y,8,8)
        self.add_line("connector",(12,20),(12,28))
        path(self,"arrow",(26,4),[("C",(34,9),(40,15),(40,22)),("C",(40,28),(34,33),(26,36))])
        self.add_polyline("arrowhead",(26,26),(26,36),(36,36))
        self.relate("connect","arrow","arrowhead")
