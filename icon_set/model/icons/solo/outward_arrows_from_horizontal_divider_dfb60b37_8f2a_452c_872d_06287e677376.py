"""Outward Arrows from Horizontal Divider.
Plan: Paired vertical outward arrows with an isolated horizontal divider. Extremes (8,4)-(40,44).
Lucide original and atomic-debug construction: move-vertical.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfb60b37-8f2a-452c-872d-06287e677376'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
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
    icon_id = 'outward-arrows-from-horizontal-divider'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('arrows', 'expand', 'vertical', 'divider', 'outward', 'resize')
    def build(self):
        self.add_line("divider",(8,24),(40,24))
        for i,s in enumerate([-1,1]):
            tip=(24,24+s*20);n=f"arrow-{i}"
            self.add_line(n,(24,24+s*8),tip)
            self.add_polyline(n+"-head",(16,24+s*12),tip,(32,24+s*12));self.relate("connect",n,n+"-head")
