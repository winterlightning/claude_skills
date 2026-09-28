"""Open End Wrench.
Plan: Diagonal shaft connects rounded hanging-hole handle to an open crescent jaw. Extremes (6,6)-(42,42).
Construction reference: local Lucide wrench, original and atomic-debug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ef6a5b2c-1e8c-5ac4-af02-c85d2d6e6b1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/wrench_ef6a5b2c-1e8c-5ac4-af02-c85d2d6e6b1e.svg'
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
    icon_id = 'open-end-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('wrench', 'spanner', 'tool', 'repair', 'jaw', 'mechanical')
    def build(self):
        path(self,"wrench",(32,6),[("L",(24,14)),("L",(32,22)),("L",(42,12)),("C",(42,18),(42,22),(40,26)),("C",(36,32),(32,32),(30,32)),("L",(27,38)),("C",(26,40),(22,42),(18,42)),("A",12,12,True,(6,30)),("C",(6,27),(7,24),(8,23)),("L",(18,15)),("C",(18,10),(24,6),(32,6))],True)
        circle(self,"hanging-hole",18,30,3)
