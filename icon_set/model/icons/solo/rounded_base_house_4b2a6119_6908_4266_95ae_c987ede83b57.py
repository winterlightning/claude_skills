"""Rounded Base House.
Plan: Mirrored roof with overhangs, equal walls and radius6 lower corners. Extremes(6,6)-(42,42).
Lucide original and atomic-debug: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b2a6119-6908-4266-95ae-c987ede83b57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_4b2a6119-6908-4266-95ae-c987ede83b57.svg'
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
    icon_id = 'rounded-base-house-4b2a6119-6908-4266-95ae-c987ede83b57'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'roof', 'building', 'outline', 'rounded')
    def build(self):
        cx=24;left=10;right=48-left;r=6
        self.add_polyline("roof",(6,24),(left,20),(cx,6),(right,20),(42,24))
        path(self,"walls",(left,20),[("L",(left,36)),("A",r,r,False,(16,42)),("L",(cx,42)),("L",(32,42)),("A",r,r,False,(right,36)),("L",(right,20))])
        self.relate("connect","roof","walls")
