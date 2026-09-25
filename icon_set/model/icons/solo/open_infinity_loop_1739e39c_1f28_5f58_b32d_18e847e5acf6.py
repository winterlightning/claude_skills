"""Open Infinity Loop.
Plan: Two smooth lobes and a rising crossing strand; free ends leave visible breaks. Extremes (4,10)-(44,38).
Lucide original and atomic-debug construction: infinity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1739e39c-1f28-5f58-b32d-18e847e5acf6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
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
    icon_id = 'open-infinity-loop'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('infinity', 'loop', 'endless', 'continuous', 'symbol', 'interface')
    def build(self):
        path(self,"loop",(18,16),[("C",(16,12),(14,10),(12,10)),("C",(7,10),(4,16),(4,24)),("C",(4,32),(7,38),(12,38)),("C",(21,38),(27,10),(36,10)),("C",(41,10),(44,16),(44,24)),("C",(44,32),(41,38),(36,38)),("C",(34,38),(32,36),(30,32))])
