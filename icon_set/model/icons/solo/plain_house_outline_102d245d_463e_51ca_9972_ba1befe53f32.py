"""Plain House Outline.
Plan: Mirrored gable, equal walls, shared lower corner radii, no interior furniture. Extremes (6,6)-(42,42).
Lucide original and atomic-debug: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '102d245d-463e-51ca-9972-ba1befe53f32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/houses_102d245d-463e-51ca-9972-ba1befe53f32.svg'
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
    icon_id = 'plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'roof', 'building', 'gable', 'outline')
    def build(self):
        cx=24;half=18;left=cx-half;right=cx+half;r=3
        path(self,"house",(cx,6),[("L",(right,22)),("L",(right,39)),("A",r,r,True,(right-r,42)),("L",(left+r,42)),("A",r,r,True,(left,39)),("L",(left,22)),("L",(cx,6))],True)
