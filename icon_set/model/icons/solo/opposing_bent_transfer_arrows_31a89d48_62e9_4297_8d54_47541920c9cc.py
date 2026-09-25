"""Opposing Bent Transfer Arrows.
Plan: Opposed bent arrows from one half-turn repeat, rounded elbows and outward tails; crossing extensions omitted for clearance. Extremes (6,6)-(42,42).
Lucide original and atomic-debug construction: arrow-down-up.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31a89d48-62e9-4297-8d54-47541920c9cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/refresh_31a89d48-62e9-4297-8d54-47541920c9cc.svg'
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
    icon_id = 'opposing-bent-transfer-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('arrows', 'transfer', 'up', 'down', 'refresh', 'exchange')
    def build(self):
        for i in range(2):
            def p(x,y):return (x,y) if i==0 else (48-x,48-y)
            n=f"arrow-{i}"
            path(self,n,p(14,6),[("L",p(14,32)),("A",4,4,True,p(10,36)),("L",p(6,36))])
            self.add_polyline(n+"-head",p(6,14),p(14,6),p(22,14));self.relate("connect",n,n+"-head")
